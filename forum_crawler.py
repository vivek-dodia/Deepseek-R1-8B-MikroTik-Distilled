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
        
        # Core RouterOS features and API sections
        self.forum_sections = {
            "2": "RouterOS",         # RouterOS General
            "49": "v7",             # RouterOS v7
            "7": "Scripts",         # Scripts (includes API)
            "31": "Routing",        # Core: Routing
            "34": "Firewall",       # Core: Firewall
            "33": "VPN",            # Core: VPN
            "35": "IPv6",           # Core: IPv6
            "32": "Wireless",       # Core: Wireless
            "36": "MPLS",           # Core: MPLS
            "37": "Queue",          # Core: Queue
            "38": "Bridge",         # Core: Bridge
            "39": "PPP",            # Core: PPP
            "40": "HotSpot",        # Core: HotSpot
            "41": "API"             # API specific
        }
        
        # Keywords to identify relevant threads
        self.relevant_keywords = [
            'api', 'rest', 'script', 'automation',
            'bgp', 'ospf', 'mpls', 'vpls',
            'firewall', 'nat', 'mangle', 'filter',
            'bridge', 'vlan', 'trunk', 'bonding',
            'vpn', 'ipsec', 'l2tp', 'sstp', 'openvpn',
            'queue', 'qos', 'shaping',
            'ppp', 'pppoe', 'pptp',
            'hotspot', 'captive', 'portal',
            'ipv6', 'dhcp', 'dns',
            'routing', 'route', 'policy',
            'configuration', 'setup', 'migration',
            'ros6', 'ros7', 'routeros'
        ]

    def clean_forum_content(self, content: str) -> str:
        """Clean forum content and preserve structure.

        This function takes raw HTML content from a forum and processes it to
        remove unnecessary elements such as navigation bars, footers, and
        scripts. It then extracts relevant information from each post, including
        the author's name, post date, and content. The cleaned posts are
        formatted into a structured string for further use.

        Args:
            content (str): The raw HTML content of the forum.

        Returns:
            str: A formatted string containing the cleaned posts, separated by "---".
        """
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove unnecessary elements
        unwanted_selectors = [
            '.postprofile', '.navbar', '.footer', '.headerbar',
            '.search-box', '.pagination', '.notice', '.rules',
            'script', 'style', '.avatar', '.signature',
            '.posting-icons', '.back2top', '.buttons',
            '#page-body > h2', '#page-footer'
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
                    content_text = content.get_text(strip=True)
                    code_blocks = content.select('code, pre')
                    has_commands = any(cmd in content_text for cmd in [
                        '/ip', '/system', '/interface', '/queue', '/routing',
                        'api', 'script', 'function', 'return'
                    ])
                    
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

    def is_relevant_thread(self, title: str, content: str) -> bool:
        """Check if a thread is relevant to core features or API.

        This function evaluates the relevance of a thread based on its title and
        content. It combines the title and content into a single lowercase
        string and checks for the presence of specific keywords that indicate
        relevance to core features or API usage. Additionally, it looks for
        common commands and code snippets that are typically associated with
        technical discussions or inquiries.

        Args:
            title (str): The title of the thread.
            content (str): The content of the thread.

        Returns:
            bool: True if the thread is relevant, False otherwise.
        """
        text = (title + " " + content).lower()
        
        # Check for relevant keywords
        has_keyword = any(keyword in text for keyword in self.relevant_keywords)
        
        # Check for code or commands
        has_code = any(cmd in text for cmd in [
            '/ip', '/system', '/interface', '/queue', '/routing',
            'api', 'rest', 'curl', 'http', 'script', 'function'
        ])
        
        return has_keyword or has_code

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

    async def get_thread_urls(self, section_id: str, crawler: AsyncWebCrawler) -> list:
        """Retrieve thread URLs from a specified forum section.

        This function constructs URLs for threads within a given section of a
        forum by iterating through the pages of that section. It utilizes an
        asynchronous web crawler to fetch the HTML content of each page, parses
        the content to extract thread links, and compiles a list of these URLs.
        The process continues until there are no more pages to retrieve or an
        error occurs.

        Args:
            section_id (str): The identifier for the forum section from which to retrieve thread URLs.
            crawler (AsyncWebCrawler): An instance of an asynchronous web crawler used to fetch page content.

        Returns:
            list: A list of strings containing the full URLs of the threads found in the
                specified section.
        """
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
                
                # Check if there's a next page
                next_page = soup.select_one('a.next')
                if not next_page:
                    break
                    
                page += 1
                await asyncio.sleep(1)
                
            except Exception as e:
                logging.error(f"Error getting threads from section {section_id}, page {page}: {str(e)}")
                break
        
        return thread_urls

    async def crawl_thread(self, url: str, crawler: AsyncWebCrawler):
        """Crawl a single forum thread and save its content if relevant.

        This method checks if the provided URL has already been visited. If not,
        it logs the crawling action, attempts to fetch the thread's HTML content
        using an asynchronous web crawler, and parses the content to extract the
        title and main content. If the thread is deemed relevant based on
        certain criteria, it cleans the content and saves it to a markdown file
        with metadata. The method also handles any exceptions that may occur
        during the crawling process.

        Args:
            url (str): The URL of the forum thread to crawl.
            crawler (AsyncWebCrawler): An instance of an asynchronous web crawler used to fetch the thread's
                content.
        """
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
                content = soup.select_one('.content')
                content_text = content.get_text(strip=True) if content else ""
                
                if self.is_relevant_thread(title, content_text):
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
keywords: {', '.join(kw for kw in self.relevant_keywords if kw in title.lower() or kw in content_text.lower())}
---

{cleaned_content}"""
                        
                        save_path.write_text(metadata, encoding="utf-8")
                        logging.info(f"Saved relevant thread: {save_path}")
                else:
                    logging.debug(f"Skipped non-relevant thread: {title}")
        
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