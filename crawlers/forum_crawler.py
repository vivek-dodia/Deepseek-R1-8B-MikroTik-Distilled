import asyncio
import logging
import re
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
            "34": "Firewall",
            "33": "VPN",
            "35": "IPv6",
            "32": "Wireless",
            "36": "MPLS",
            "37": "Queue",
            "38": "Bridge",
            "39": "PPP",
            "40": "HotSpot",
            "41": "API"
        }

        self.section_keywords = {
            "RouterOS": ['routeros', 'ros6', 'ros7', 'v6', 'v7', 'configuration', 'setup'],
            "v7": ['v7', 'ros7', 'routeros7', 'upgrade', 'migration'],
            "Scripts": ['script', 'function', 'scheduler', 'netwatch', 'automation'],
            "Routing": ['bgp', 'ospf', 'rip', 'routing', 'route', 'gateway', 'path'],
            "Firewall": ['firewall', 'nat', 'filter', 'mangle', 'raw', 'connection'],
            "VPN": ['vpn', 'ipsec', 'l2tp', 'pptp', 'sstp', 'wireguard', 'openvpn'],
            "IPv6": ['ipv6', 'address', 'neighbor', 'dhcpv6', 'prefix', 'route6'],
            "Wireless": ['wireless', 'wifi', 'wlan', 'radio', 'channel', 'band'],
            "MPLS": ['mpls', 'vpls', 'ldp', 'label', 'tunnel', 'transport'],
            "Queue": ['queue', 'qos', 'traffic', 'bandwidth', 'limit', 'priority'],
            "Bridge": ['bridge', 'switch', 'vlan', 'spanning-tree', 'port'],
            "PPP": ['ppp', 'pppoe', 'profile', 'secret', 'client', 'server'],
            "HotSpot": ['hotspot', 'login', 'user', 'profile', 'walled-garden'],
            "API": ['api', 'rest', 'http', 'request', 'response', 'json']
        }

        self.relevant_keywords = [
            'routeros', 'ros6', 'ros7', 'v6', 'v7',
            'firewall', 'nat', 'routing', 'vpn', 'bridge',
            'interface', 'wireless', 'queue', 'mpls', 'ppp',
            'hotspot', 'ipv6', 'api', 'script', 'vlan',
            'bgp', 'ospf', 'rip', 'igmp', 'pim',
            'configuration', 'setup', 'howto', 'solution',
            'problem', 'error', 'help', 'example', 'issue'
        ]

    def has_code_blocks(self, content):
        """Check if content has configuration or code blocks"""
        code_indicators = [
            '/interface', '/ip', '/system', '/routing',
            'script:', 'function', ':foreach', ':if',
            '# Script', '# Config', '```'
        ]
        return any(indicator in content for indicator in code_indicators)

    def is_technical_content(self, content, section):
        """Check if content is technically relevant"""
        if section in self.section_keywords:
            section_terms = self.section_keywords[section]
            if any(term in content.lower() for term in section_terms):
                return True
        
        return any(term in content.lower() for term in self.relevant_keywords)

    def is_valuable_thread(self, content, title, section, post_count):
        """Determine if thread should be saved"""
        if not content or len(content) < 200:  # Minimum content length
            return False

        if post_count < 2:  # Require at least 2 posts
            return False

        # Must have either code blocks or technical content
        has_technical = self.is_technical_content(content, section)
        has_code = self.has_code_blocks(content)
        
        return has_technical or has_code

    async def crawl_thread(self, url: str, crawler: AsyncWebCrawler, section: str):
        if url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        logging.info(f"Crawling: {url}")
        
        try:
            await asyncio.sleep(1)
            result = await crawler.arun(url, config=self.run_config)
            
            if not result.success:
                return

            soup = BeautifulSoup(result.html, 'html.parser')
            
            thread_id = None
            if 't=' in url:
                thread_id = re.search(r't=(\d+)', url).group(1)
            elif 'p=' in url:
                thread_id = re.search(r'p=(\d+)', url).group(1)
                
            if not thread_id:
                return
                
            posts = soup.find_all('div', class_='post')
            logging.info(f"Found {len(posts)} posts in {url}")

            if not posts:
                return

            thread_content = []
            full_content = ""
            
            for idx, post in enumerate(posts, 1):
                try:
                    author = post.find('div', class_='author')
                    content = post.find('div', class_='content')
                    date = post.find('div', class_='date')
                    
                    if content:
                        post_text = content.get_text(strip=True)
                        full_content += post_text + "\n"
                        
                        formatted_post = f"### Post {idx}\n"
                        formatted_post += f"Author: {author.get_text(strip=True) if author else 'Unknown'}\n"
                        formatted_post += f"Date: {date.get_text(strip=True) if date else 'Unknown'}\n\n"
                        formatted_post += post_text
                        formatted_post += "\n\n---\n"
                        thread_content.append(formatted_post)
                except Exception as e:
                    logging.error(f"Error processing post {idx}: {e}")
                    continue

            title = soup.find('h2', class_='topic-title')
            title = title.get_text(strip=True) if title else f"Thread-{thread_id}"

            if self.is_valuable_thread(full_content, title, section, len(posts)):
                save_path = self.base_save_path / f"thread_{thread_id}.md"
                save_path.parent.mkdir(parents=True, exist_ok=True)

                metadata = f"""---
title: {title}
url: {url}
thread_id: {thread_id}
section: {section}
post_count: {len(posts)}
date_crawled: {datetime.now().isoformat()}
---

{''.join(thread_content)}"""

                save_path.write_text(metadata, encoding='utf-8')
                logging.info(f"Saved valuable thread: {save_path}")
            else:
                logging.debug(f"Skipped non-valuable thread: {url}")

        except Exception as e:
            logging.error(f"Error processing {url}: {e}")

    async def crawl_section(self, section_id: str, crawler: AsyncWebCrawler):
        section_name = self.forum_sections.get(section_id, "Unknown")
        page = 0
        
        while True:
            url = f"{self.base_forum_url}/viewforum.php?f={section_id}&start={page * 50}"
            logging.info(f"Scanning page {page} of section {section_name}")
            
            result = await crawler.arun(url, config=self.run_config)
            if not result.success:
                break

            soup = BeautifulSoup(result.html, 'html.parser')
            links = [a for a in soup.find_all('a') if 'viewtopic.php' in str(a.get('href', ''))]
            
            if not links:
                break

            for link in links:
                thread_url = urljoin(self.base_forum_url, link['href'])
                await self.crawl_thread(thread_url, crawler, section_name)
                await asyncio.sleep(1)

            page += 1
            await asyncio.sleep(2)

    async def crawl(self):
        self.base_save_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Starting crawl, saving to: {self.base_save_path}")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for section_id, section_name in self.forum_sections.items():
                logging.info(f"Processing section: {section_name} (ID: {section_id})")
                await self.crawl_section(section_id, crawler)

if __name__ == "__main__":
    crawler = MikroTikForumCrawler()
    asyncio.run(crawler.crawl())