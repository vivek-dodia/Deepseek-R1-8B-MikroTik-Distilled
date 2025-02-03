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
        
        # Forum sections to crawl
        self.forum_sections = {
            "2": "RouterOS",         # RouterOS General
            "49": "v7",             # RouterOS v7
            "7": "Scripts",         # Scripts
            "31": "Routing",        # Routing
            "34": "Firewall",       # Firewall
            "33": "VPN",            # VPN
            "35": "IPv6",           # IPv6
            "32": "Wireless",       # Wireless
            "36": "MPLS",           # MPLS
            "37": "Queue",          # Queue
            "38": "Bridge",         # Bridge
            "39": "PPP",            # PPP
            "40": "HotSpot",        # HotSpot
            "41": "API",            # API
        }

        # Keywords for identifying relevant content
        self.relevant_keywords = [
            # RouterOS versions
            'routeros', 'ros6', 'ros7', 'v6', 'v7',
            # Core features
            'firewall', 'nat', 'routing', 'vpn', 'bridge',
            'interface', 'wireless', 'queue', 'mpls', 'ppp',
            'hotspot', 'ipv6', 'api', 'script', 'vlan',
            # Protocols
            'bgp', 'ospf', 'rip', 'igmp', 'pim',
            # Common terms
            'configuration', 'setup', 'howto', 'solution',
            'problem', 'error', 'help', 'example', 'issue'
        ]
        
        # Networking and configuration terms
        self.networking_terms = [
            'router', 'network', 'config', 'setup', 'mikrotik',
            'interface', 'address', 'gateway', 'dns', 'dhcp',
            'port', 'switch', 'connect', 'traffic', 'bandwidth',
            'error', 'problem', 'solution', 'help', 'how to'
        ]

    def clean_forum_content(self, content: str) -> str:
        """Clean forum content and preserve structure"""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove minimal unnecessary elements
        unwanted_selectors = [
            'script', 'style', '.signature',
            '.posting-icons', '.back2top', '.buttons'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()

        posts = []
        for post in soup.select('.post'):
            try:
                author = post.select_one('.author')
                content = post.select_one('.content')
                date = post.select_one('.date')
                
                if author and content:
                    post_data = f"""### Author: {author.get_text(strip=True)}
Date: {date.get_text(strip=True) if date else 'Unknown'}

{self.format_post_content(content)}

"""
                    posts.append(post_data)
            except Exception as e:
                logging.error(f"Error processing post: {str(e)}")
                continue
        
        return "\n---\n".join(posts)

    def format_post_content(self, content_element) -> str:
        """Format post content preserving code blocks and structure"""
        formatted_content = []
        
        # Process code blocks first
        for code in content_element.select('code, pre, .codebox'):
            code_text = code.get_text(strip=True)
            if code_text:
                formatted_content.append(f"```\n{code_text}\n```")
            code.decompose()
        
        # Get remaining text
        text = content_element.get_text(strip=True)
        if text:
            formatted_content.append(text)
        
        return "\n\n".join(formatted_content)

    def has_mikrotik_commands(self, text: str) -> bool:
        """Check if text contains MikroTik commands or configurations"""
        commands = [
            '/ip', '/system', '/interface', '/queue', '/routing',
            '/ppp', '/mpls', '/tool', '/user', '/snmp', '/radius',
            'api', 'rest', 'curl', 'http', 'script', 'function',
            'set', 'add', 'print', 'enable', 'disable', 'remove'
        ]
        return any(cmd in text.lower() for cmd in commands)

    def is_relevant_thread(self, title: str, content: str) -> bool:
        """Check if thread is relevant with looser criteria"""
        text = (title + " " + content).lower()
        
        # Check for any relevant content
        has_relevance = (
            any(keyword in text for keyword in self.relevant_keywords) or
            any(term in text for term in self.networking_terms) or
            self.has_mikrotik_commands(text)
        )
        
        return has_relevance

    async def get_thread_urls(self, section_id: str, crawler: AsyncWebCrawler) -> list:
        """Get thread URLs from a forum section"""
        thread_urls = []
        page = 0
        
        while True:
            url = f"{self.base_forum_url}/viewforum.php?f={section_id}&start={page * 50}"
            logging.info(f"Getting page {page} from section {section_id}")
            
            try:
                result = await crawler.arun(url, config=self.run_config)
                if not result.success:
                    break
                
                soup = BeautifulSoup(result.html, 'html.parser')
                topics = soup.select('.topictitle')
                if not topics:
                    break
                
                for topic in topics:
                    href = topic.get('href')
                    if href:
                        full_url = urljoin(self.base_forum_url, href)
                        thread_urls.append(full_url)
                
                if not soup.select_one('a.next'):
                    break
                    
                page += 1
                await asyncio.sleep(1)
                
            except Exception as e:
                logging.error(f"Error getting threads from section {section_id}, page {page}: {str(e)}")
                break
        
        return thread_urls

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
                
                if cleaned_content.strip():
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
        logging.info(f"Starting forum crawl, saving to: {self.base_save_path}")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for section_id, section_name in self.forum_sections.items():
                logging.info(f"Processing forum section: {section_name} (ID: {section_id})")
                thread_urls = await self.get_thread_urls(section_id, crawler)
                logging.info(f"Found {len(thread_urls)} threads in section {section_name}")
                
                for i in range(0, len(thread_urls), 2):
                    batch = thread_urls[i:i+2]
                    tasks = [self.crawl_thread(url, crawler) for url in batch]
                    await asyncio.gather(*tasks)
                    await asyncio.sleep(2)
                    logging.info(f"Completed batch {i//2 + 1} of {(len(thread_urls) + 1)//2} in section {section_name}")

if __name__ == "__main__":
    crawler = MikroTikForumCrawler()
    asyncio.run(crawler.crawl())