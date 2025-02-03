import asyncio
import logging
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("forum_crawler.log"), logging.StreamHandler()]
)

class MikroTikForumCrawler:
    def __init__(self):
        self.visited_urls = set()
        self.base_save_path = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\forum")
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(word_count_threshold=0)
        self.base_forum_url = "https://forum.mikrotik.com"
        
        self.forum_sections = {
            "2": "RouterOS",
            "49": "v7",
            "7": "Scripts",
            "31": "Routing",
        }

    def clean_post_content(self, element):
        if not element:
            return ""
        for tag in element.find_all(['script', 'style']):
            tag.decompose()
        return element.get_text(strip=True, separator='\n')

    async def crawl_thread(self, url: str, crawler: AsyncWebCrawler):
        if url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        logging.info(f"Processing: {url}")
        
        try:
            result = await crawler.arun(url, config=self.run_config)
            if not result.success:
                return

            soup = BeautifulSoup(result.html, 'html.parser')
            posts = soup.find_all('div', class_='post')
            logging.info(f"Found {len(posts)} posts in {url}")

            if not posts:
                return

            thread_content = []
            for post in posts:
                author = post.find('div', class_='author')
                content = post.find('div', class_='content')
                date = post.find('div', class_='date')

                if content:
                    clean_content = self.clean_post_content(content)
                    if len(clean_content) > 10:
                        post_text = f"### Author: {author.get_text(strip=True) if author else 'Unknown'}\n"
                        post_text += f"Date: {date.get_text(strip=True) if date else 'Unknown'}\n\n"
                        post_text += f"{clean_content}\n\n---\n"
                        thread_content.append(post_text)

            if thread_content:
                thread_id = url.split('t=')[-1].split('&')[0]
                title = soup.find('h2', class_='topic-title')
                title = title.get_text(strip=True) if title else f"Thread-{thread_id}"

                save_path = self.base_save_path / f"thread_{thread_id}.md"
                save_path.parent.mkdir(parents=True, exist_ok=True)

                content = f"""---
title: {title}
url: {url}
date: {datetime.now().isoformat()}
---

{''.join(thread_content)}"""

                save_path.write_text(content, encoding='utf-8')
                logging.info(f"Saved: {save_path}")

        except Exception as e:
            logging.error(f"Error on {url}: {e}")

    async def crawl_section(self, section_id: str, crawler: AsyncWebCrawler):
        page = 0
        while True:
            url = f"{self.base_forum_url}/viewforum.php?f={section_id}&start={page * 50}"
            logging.info(f"Scanning page {page} of section {section_id}")

            result = await crawler.arun(url, config=self.run_config)
            if not result.success:
                break

            soup = BeautifulSoup(result.html, 'html.parser')
            topic_links = [link for link in soup.find_all('a') 
                         if 'viewtopic.php' in link.get('href', '')]

            if not topic_links:
                break

            for link in topic_links:
                thread_url = urljoin(self.base_forum_url, link['href'])
                await self.crawl_thread(thread_url, crawler)
                await asyncio.sleep(1)

            page += 1
            await asyncio.sleep(2)

    async def crawl(self):
        self.base_save_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Starting crawl, saving to: {self.base_save_path}")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for section_id in self.forum_sections:
                await self.crawl_section(section_id, crawler)

if __name__ == "__main__":
    crawler = MikroTikForumCrawler()
    asyncio.run(crawler.crawl())