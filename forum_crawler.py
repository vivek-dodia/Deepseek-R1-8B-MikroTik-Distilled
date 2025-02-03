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
            "router+os+7+upgrade",
            "routeros+7+configuration",
            "ros+7+migration",
            "routeros+7+scripting",
            "ros+7+firewall",
            "ros+7+routing"
        ]

    def clean_forum_content(self, content: str) -> str:
        """Clean forum content and preserve structure.

        This function takes raw HTML content from a forum and processes it to
        remove unnecessary elements such as navigation bars, footers, and
        scripts. It extracts relevant information from each post, including the
        author, date, and content, while preserving the structure of the posts.
        The cleaned content is formatted and returned as a string. This is
        particularly useful for displaying forum posts in a more readable
        format.

        Args:
            content (str): The raw HTML content of the forum.

        Returns:
            str: A formatted string containing the cleaned forum posts.
        """
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
        """Format post content preserving code blocks and structure.

        This function processes the given content element to format its content
        by preserving code blocks and maintaining the overall structure. It
        first extracts and formats any code blocks found within the content,
        wrapping them in triple backticks for proper Markdown representation.
        After processing the code blocks, it retrieves the remaining text
        content and appends it to the formatted output.

        Args:
            content_element (BeautifulSoup): A BeautifulSoup object representing

        Returns:
            str: The formatted post content as a string, with code blocks
            properly wrapped and other text included.
        """
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
        """Search for forum topics based on a specific query.

        This function constructs a search URL using the provided query and
        performs an asynchronous request to the forum's search endpoint. It
        parses the resulting HTML to extract URLs of the topics that match the
        search criteria. If the search is successful, it returns a list of topic
        URLs. In case of any errors during the search, it logs the error and
        returns an empty list.

        Args:
            query (str): The search query to find relevant forum topics.
            crawler (AsyncWebCrawler): An instance of AsyncWebCrawler used
                to perform the asynchronous web request.

        Returns:
            list: A list of URLs for the topics found in the forum.
        """
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
        """Crawl a single forum thread and save its content.

        This method checks if the provided URL has already been visited. If not,
        it logs the crawling process, retrieves the thread's HTML content using
        the provided crawler, and extracts relevant information such as the
        thread title and cleaned content. If the content is valid, it saves the
        data in a markdown file with appropriate metadata.

        Args:
            url (str): The URL of the forum thread to crawl.
            crawler (AsyncWebCrawler): An instance of AsyncWebCrawler used to fetch the thread content.
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
        """Main function to initiate the crawling process for forum content.

        This function sets up the necessary directory for saving the crawled
        data and utilizes an asynchronous web crawler to search for forum
        threads based on predefined search queries. For each query, it processes
        the results in batches to crawl individual threads while respecting
        server load by introducing a delay between batches.  It logs the
        progress of the crawling operation, including the number of threads
        found for each query and the completion of each batch.
        """
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