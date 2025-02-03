import asyncio
import logging
from pathlib import Path
from urllib.parse import urljoin, urlparse, quote
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from datetime import datetime
from urllib import parse

# Configure logging to a file in the specified directory
log_dir = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "forum_crawler.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
)

class MikroTikForumCrawler:
    def __init__(self):
        self.base_save_path = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\forum")
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(word_count_threshold=0)
        self.base_forum_url = "https://forum.mikrotik.com"
        
        # Main forum sections
        self.forum_sections = {
            "2": "RouterOS",          # RouterOS General
            "49": "v7",              # RouterOS v7
            "7": "Scripts",          # Scripts
            "31": "Routing",         # Routing
            "34": "Firewall",        # Firewall
            "33": "VPN",            # VPN
            "35": "IPv6",           # IPv6
            "32": "Wireless",       # Wireless
            "23": "CAPsMAN",        # CAPsMAN
            "8": "Hardware",        # Hardware
            "15": "Troubleshooting" # Troubleshooting
        }
        
        # Extended search terms
        self.search_terms = [
            # Core features
            'bgp configuration', 'ospf setup', 'mpls vpls',
            'firewall rules', 'nat configuration', 'vpn tunnel',
            'queue management', 'bridge setup', 'vlan config',
            # Authentication and security
            'authentication setup', 'certificates', 'ipsec config',
            'hotspot setup', 'ppp configuration',
            # Automation and scripting
            'script example', 'api usage', 'automation',
            'scheduler setup', 'netwatch config',
            # Common scenarios
            'isp setup', 'enterprise config', 'failover setup',
            'load balancing', 'high availability'
        ]

    def build_search_urls(self, section_id: str = None) -> list:
        """Generate search URLs for the forum"""
        urls = []
        
        # Section specific searches
        if section_id:
            base_urls = [
                f"{self.base_forum_url}/search.php?fid[]={section_id}&sc=1&sr=topics&sk=t&sd=d",
                f"{self.base_forum_url}/search.php?fid[]={section_id}&sc=1&sr=topics&sk=v&sd=d",
                f"{self.base_forum_url}/viewforum.php?f={section_id}&sort=desc"
            ]
            urls.extend(base_urls)
        
        # Add keyword searches
        for term in self.search_terms:
            search_url = f"{self.base_forum_url}/search.php?keywords={quote(term)}&terms=all&sc=1&sr=topics&sk=t&sd=d"
            if section_id:
                search_url += f"&fid[]={section_id}"
            urls.append(search_url)
        
        return urls

    def clean_forum_content(self, content: str) -> str:
        """Clean and format forum content"""
        soup = BeautifulSoup(content, 'html.parser')
        
        unwanted_selectors = [
            'script', 'style', '.signature',
            '.posting-icons', '.back2top', '.buttons',
            '.header', '.footer', '.navbar'
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
        """Format post content preserving structure"""
        formatted_content = []
        
        # Process code blocks
        for code in content_element.select('code, pre, .codebox'):
            code_text = code.get_text(strip=True)
            if code_text:
                formatted_content.append(f"```\n{code_text}\n```")
            code.decompose()
        
        # Process quotes
        for quote in content_element.select('blockquote'):
            quote_text = quote.get_text(strip=True)
            if quote_text:
                formatted_content.append(f"> {quote_text}")
            quote.decompose()
        
        # Get remaining text
        text = content_element.get_text(strip=True)
        if text:
            formatted_content.append(text)
        
        return "\n\n".join(formatted_content)

    def has_valuable_content(self, text: str) -> bool:
        """Check if content contains valuable information"""
        # Relax the check for debugging
        return len(text) > 100

    def build_forum_urls(self, section_id: str) -> list:
        """Generate different view URLs for forum sections"""
        return [
            f"{self.base_forum_url}/viewforum.php?f={section_id}&start=",  # Latest posts
            f"{self.base_forum_url}/viewforum.php?f={section_id}&sort=views&start=",  # Most viewed
            f"{self.base_forum_url}/viewforum.php?f={section_id}&sort=replies&start="  # Most replies
        ]


    async def get_thread_urls(self, crawler: AsyncWebCrawler, section_id: str = None) -> set:
        """Get thread URLs from forum section with pagination"""
        thread_urls = set()
        base_urls = []
        
        if section_id:
          base_urls = self.build_forum_urls(section_id)
        else:
          # Generate base_urls for all sections.
          for section_id in self.forum_sections:
            base_urls.extend(self.build_forum_urls(section_id))
        
        
        for base_url in base_urls:
            page = 0
            while True:
                url = f"{base_url}{page * 50}"
                logging.info(f"Getting page {page} from {url}")
                
                try:
                    # Add delay between requests
                    await asyncio.sleep(2)
                    
                    result = await crawler.arun(url, config=self.run_config)
                    logging.info(f"Result for {url} was successful: {result.success}")
                    if not result.success:
                        break
                    
                    soup = BeautifulSoup(result.html, 'html.parser')
                    topics = soup.select('.topictitle')
                    
                    if not topics:
                        logging.info(f"No topics found for {url}")
                        break
                        
                    for topic in topics:
                        href = topic.get('href')
                        if href and 'viewtopic.php' in href:
                            full_url = urljoin(self.base_forum_url, href)
                            
                            # Remove the session ID from the URL
                            parsed_url = urlparse(full_url)
                            query_params = dict(parse.parse_qsl(parsed_url.query))
                            query_params.pop('sid', None)
                            
                            cleaned_query = parse.urlencode(query_params)
                            cleaned_full_url = parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, cleaned_query, parsed_url.fragment))
                            
                            thread_urls.add(cleaned_full_url)
                            logging.info(f"Found thread url {cleaned_full_url}")
                        else:
                           logging.info(f"Skipping non-thread URL {href}")
                    
                    # Check for next page
                    if not soup.select('.pagination'):
                        break
                        
                    page += 1
                    
                except Exception as e:
                    logging.error(f"Error on page {page}: {str(e)}")
                    break
        
        return thread_urls

    async def crawl_thread(self, url: str, crawler: AsyncWebCrawler):
        """Crawl and save thread content"""
        if url in self.visited_urls:
          return
        
        self.visited_urls.add(url)
        logging.info(f"Crawling thread: {url}")
        
        try:
            logging.info(f"Fetching thread content from {url}")
            result = await crawler.arun(url, config=self.run_config)
            
            if result.success:
                logging.info(f"Successfully fetched thread content from {url}")
                soup = BeautifulSoup(result.html, 'html.parser')
                title = soup.select_one('.topic-title')
                title = title.get_text(strip=True) if title else "Untitled Thread"
                
                content = soup.select_one('.content')
                if content:
                    logging.info(f"Found content element for thread {url}")
                    if self.has_valuable_content(content.get_text()):
                        logging.info(f"Thread {url} has valuable content")
                        cleaned_content = self.clean_forum_content(result.html)
                        
                        if cleaned_content.strip():
                            thread_id = url.split('t=')[-1].split('&')[0]
                            save_path = self.base_save_path / f"thread_{thread_id}.md"
                            logging.info(f"Saving to path {save_path}")
                            
                            if not save_path.exists():  # Only save if we don't have it
                                save_path.parent.mkdir(parents=True, exist_ok=True)
                                
                                metadata = f"""---
title: {title}
source_url: {url}
crawled_date: {datetime.now().isoformat()}
type: forum_thread
---

{cleaned_content}"""
                                
                                save_path.write_text(metadata, encoding="utf-8")
                                logging.info(f"Saved new thread: {save_path}")
                            else:
                                logging.info(f"Thread {save_path} exists, skipping save")
                        else:
                            logging.info(f"Cleaned content was empty for thread {url}")
                    else:
                        logging.info(f"Thread {url} did not have valuable content")
                else:
                   logging.info(f"Thread {url} could not find content element")
            else:
                logging.info(f"Failed to fetch content for thread {url}")
        except Exception as e:
            logging.error(f"Failed thread {url}: {str(e)}")
            
    async def test_crawl(self):
         """Test crawl function"""
         test_url = "https://forum.mikrotik.com/viewtopic.php?f=2&t=213221&p=1114399#p1114399"
         async with AsyncWebCrawler(config=self.browser_config) as crawler:
             await self.crawl_thread(test_url, crawler)

    async def crawl(self):
        """Main crawling function"""
        self.base_save_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Starting forum crawl, saving to: {self.base_save_path}")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            
            # First crawl each section
            for section_id, section_name in self.forum_sections.items():
                logging.info(f"Processing section: {section_name} (ID: {section_id})")
                thread_urls = await self.get_thread_urls(crawler, section_id)
                logging.info(f"Found {len(thread_urls)} threads in {section_name}")
                
                self.visited_urls = set()  # Reset visited_urls
                for url in thread_urls:
                  await self.crawl_thread(url, crawler)
                  await asyncio.sleep(1)
            
            # Then do a general search across all sections
            logging.info("Performing general forum search")
            thread_urls = await self.get_thread_urls(crawler)
            logging.info(f"Found {len(thread_urls)} additional threads")
            
            self.visited_urls = set() # Reset visited_urls
            for url in thread_urls:
              await self.crawl_thread(url, crawler)
              await asyncio.sleep(1)

if __name__ == "__main__":
    crawler = MikroTikForumCrawler()
    async def main():
        # Run the test_crawl function
        # await crawler.test_crawl()
        # You can use this to see if regular crawl works after test_crawl
        await crawler.crawl()
    asyncio.run(main())