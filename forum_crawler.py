import asyncio
import logging
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
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
        
        # Priority forums
        self.priority_forums = {
            "2": "RouterOS",     # RouterOS General
            "7": "Scripts",      # Scripts
            "49": "v7",         # RouterOS v7 specific forum
            "31": "Routing",    # Routing Protocols
            "32": "Wireless"    # Wireless configurations
        }
        
        # Search queries focused on RouterOS 7
        self.search_queries = [
    # RouterOS 7 specific
    "routeros+7",
    "ros+7",
    # RouterOS 6 and 7 common topics
    "routeros+solved",
    "mikrotik+script+solved",
    "mikrotik+firewall+solved",
    "mikrotik+routing+solved",
    "mikrotik+vpn+solved",
    "mikrotik+vlan+solved",
    "mikrotik+bridge+solved",
    "mikrotik+wireless+solved",
    "mikrotik+configuration+solved",
    # Common use cases
    "mikrotik+bgp+solved",
    "mikrotik+ospf+solved",
    "mikrotik+nat+solved",
    "mikrotik+ipsec+solved",
    "mikrotik+queue+solved",
    "mikrotik+hotspot+solved",
    "mikrotik+pppoe+solved"
]

    def clean_forum_content(self, content: str) -> str:
        """Clean forum content and preserve structure"""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove unnecessary elements
        unwanted_selectors = [
            '.postprofile', '.navbar', '.footer', '.headerbar',
            '.search-box', '.pagination', '.notice', '.rules',
            'script', 'style', '.avatar', '.signature',
            '.posting-icons', '.back2top', '.buttons'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()

        posts = []
        for post in soup.select('.post'):
            try:
                # Extract post information
                author = post.select_one('.author')
                content = post.select_one('.content')
                date = post.select_one('.date')
                
                if author and content:
                    # Clean the content text
                    content_text = content.get_text(strip=True)
                    
                    # Check if post contains code or commands
                    code_blocks = content.select('code, pre')
                    has_commands = any(cmd in content_text for cmd in ['/ip', '/system', '/interface'])
                    
                    post_data = f"""### Author: {author.get_text(strip=True)}
Date: {date.get_text(strip=True) if date else 'Unknown'}

{self.format_post_content(content)}

"""
                    if code_blocks or has_commands:
                        posts.append(post_data)
            except Exception as e:
                logging.error(f"Error processing post: {str(e)}")
                continue
        
        return "\n---\n".join(posts)

    def format_post_content(self, content_element) -> str:
        """Format post content preserving code blocks and structure"""
        formatted_content = []
        
        # Process code blocks first
        for code in content_element.select('code, pre'):
            code_text = code.get_text(strip=True)
            if code_text:
                formatted_content.append(f"```\n{code_text}\n```")
            code.decompose()
        
        # Get remaining text
        text = content_element.get_text(strip=True)
        if text:
            formatted_content.append(text)
        
        return "\n\n".join(formatted_content)

    async def search_forum(self, query: str, crawler: AsyncWebCrawler) -> list:
        """Search forum with specific query"""
        search_url = f"{self.base_forum_url}/search.php?keywords={query}&terms=all&author=&sc=1&sf=titleonly&sr=topics&sk=t&sd=d&st=0&ch=300&t=0&submit=Search"
        
        try:
            result = await crawler.arun(search_url, config=self.run_config)
            thread_urls = []
            
            if result.success:
                soup = BeautifulSoup(result.html, 'html.parser')
                for topic in soup.select('.topictitle'):
                    href = topic.get('href')
                    if href:
                        thread_urls.append(urljoin(self.base_forum_url, href))
            
            return thread_urls
        except Exception as e:
            logging.error(f"Error searching forum: {str(e)}")
            return []

    async def crawl_thread(self, url: str, crawler: AsyncWebCrawler):
        """Crawl a single forum thread"""
        if url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        logging.info(f"Crawling thread: {url}")
        
        try:
            result = await crawler.arun(url, config=self.run_config)
            
            if result.success:
                soup = BeautifulSoup(result.html, 'html.parser')
                title = soup.select_one('.topic-title')
                title = title.get_text(strip=True) if title else "Untitled Thread"
                
                cleaned_content = self.clean_forum_content(result.html)
                
                if cleaned_content.strip():  # Only save if there's actual content
                    # Create a clean filename from the thread ID
                    thread_id = url.split('t=')[-1].split('&')[0]
                    save_path = self.base_save_path / f"thread_{thread_id}.md"
                    save_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    metadata = f"""---
title: {title}
source_url: {url}
crawled_date: {datetime.now().isoformat()}
section: mikrotik_forum
type: forum_thread
---

{cleaned_content}"""
                    
                    save_path.write_text(metadata, encoding="utf-8")
                    logging.info(f"Saved thread: {save_path}")
        
        except Exception as e:
            logging.error(f"Failed thread {url}: {str(e)}")

    async def crawl(self):
        """Main crawling function"""
        self.base_save_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Saving forum content to: {self.base_save_path}")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for query in self.search_queries:
                logging.info(f"Processing search query: {query}")
                thread_urls = await self.search_forum(query, crawler)
                logging.info(f"Found {len(thread_urls)} threads for query: {query}")
                
                for i in range(0, len(thread_urls), 2):
                    batch = thread_urls[i:i+2]
                    tasks = [self.crawl_thread(url, crawler) for url in batch]
                    await asyncio.gather(*tasks)
                    await asyncio.sleep(2)  # Be nice to the server
                    logging.info(f"Completed batch {i//2 + 1} of {(len(thread_urls) + 1)//2}")

if __name__ == "__main__":
    crawler = MikroTikForumCrawler()
    asyncio.run(crawler.crawl())