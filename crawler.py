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
    handlers=[logging.FileHandler("crawler.log"), logging.StreamHandler()]
)

class MikroTikDocCrawler:
    def __init__(self):
        self.visited_urls = set()
        self.base_save_path = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data")
        self.browser_config = BrowserConfig(headless=True)
        self.run_config = CrawlerRunConfig(word_count_threshold=0)  # Only using supported parameter
        
    def load_urls(self, file_path: str) -> list:
        """Load URLs from a text file"""
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        logging.info(f"Loaded {len(urls)} URLs from {file_path}")
        return urls

    def get_save_path(self, url: str) -> Path:
        """Generate save path maintaining documentation hierarchy"""
        parsed = urlparse(url)
        path_parts = parsed.path.split('/')
        page_name = path_parts[-1].replace('+', '_')
        save_path = self.base_save_path / 'mikrotik_docs' / page_name
        save_path.parent.mkdir(parents=True, exist_ok=True)
        return save_path.with_suffix('.md')

    def clean_content(self, content: str) -> str:
        """Clean and format the content"""
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove unwanted elements
        unwanted_selectors = [
            '.page-tree', '.breadcrumbs', '.footer', '.header',
            '.confluence-information-macro', '.space-tools',
            '.hide-if-space-pages', '.page-metadata', '.page-operations',
            'script', 'style', '#navigation', '#header', '#footer',
            '#sidebar', '.nav', '.confluence-jim-macro',
            '.space-tools', '.page-restrictions', '.page-metadata',
            '.page-bottombanner', '.logged-out', '.aui-page-header',
            '.ia-secondary-header', '.theme-default',
            '.expand-collapse-content', '.plugin_pagetree',
            '.plugin-space', '.aui-page-panel',
            '#login-link', '#quick-search', '#navigation-panel',
            '.page-tools', '.aui-buttons',
            '.page-metadata-modification-info'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()
    
        # Process content by sections
        sections = []
        current_section = []
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'table', 'ul', 'ol', 'pre', 'code']):
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Save previous section
                if current_section:
                    sections.append('\n'.join(current_section))
                    current_section = []
                
                # Add header
                level = int(element.name[1])
                text = element.get_text(strip=True)
                if text:
                    current_section.append(f"\n{'#' * level} {text}")
            
            elif element.name == 'table':
                rows = []
                headers = [th.get_text(strip=True) for th in element.find_all('th')]
                
                if headers:
                    rows.append(' | '.join(headers))
                    rows.append('-' * len(' | '.join(headers)))
                
                for row in element.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in row.find_all('td')]
                    if cells:
                        rows.append(' | '.join(cells))
                
                if rows:
                    current_section.extend([''] + rows + [''])
            
            elif element.name in ['ul', 'ol']:
                for li in element.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    if text:
                        current_section.append(f"* {text}")
                current_section.append('')  # Add space after lists
            
            elif element.name in ['pre', 'code']:
                code = element.get_text(strip=True)
                if code:
                    current_section.extend(['', '```', code, '```', ''])
            
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text and not any(skip in text.lower() for skip in 
                    ['powered by', 'atlassian', 'confluence', 'skip to', 'log in']):
                    current_section.append(text)
        
        # Add last section
        if current_section:
            sections.append('\n'.join(current_section))
        
        # Join all sections with proper spacing
        clean_text = '\n\n'.join(section.strip() for section in sections if section.strip())
        
        # Final cleanup
        clean_text = clean_text.replace('\n\n\n', '\n\n')
        clean_text = '\n'.join(line for line in clean_text.splitlines() 
                             if line.strip() or line.startswith('#'))
        
        return clean_text

    async def crawl_page(self, url: str, crawler: AsyncWebCrawler):
        """Crawl a single page and extract its content"""
        if url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        logging.info(f"Crawling: {url}")
        
        try:
            result = await crawler.arun(url, config=self.run_config)
            
            if result.success:
                logging.info(f"Successfully fetched {url}")
                
                # Try both HTML and markdown content
                content = result.html if result.html else result.markdown
                if not content:
                    logging.error(f"No content retrieved for {url}")
                    return
                    
                logging.info(f"Content length: {len(content)}")
                
                # Parse with BeautifulSoup to check content
                soup = BeautifulSoup(content, 'html.parser')
                
                # Try different content selectors
                main_content = (
                    soup.select_one('.wiki-content') or 
                    soup.select_one('main') or 
                    soup.select_one('#main-content') or 
                    soup.select_one('.content') or
                    soup.select_one('body')  # Fallback to body if nothing else found
                )
                
                if main_content:
                    cleaned_content = self.clean_content(str(main_content))
                    
                    # Get title
                    title = soup.find('h1')
                    if not title:
                        title = soup.find('title')
                    title = title.get_text(strip=True) if title else "Untitled"
                    
                    metadata = f"""---
title: {title}
source_url: {url}
crawled_date: {datetime.now().isoformat()}
section: mikrotik_docs
type: documentation
---

{cleaned_content}"""
                    
                    save_path = self.get_save_path(url)
                    save_path.write_text(metadata, encoding="utf-8")
                    logging.info(f"Saved: {save_path} with content length {len(cleaned_content)}")
                else:
                    logging.error(f"No main content found for {url}")
                    
            else:
                logging.error(f"Crawl failed for {url}: {result.error if hasattr(result, 'error') else 'Unknown error'}")
                
        except Exception as e:
            logging.error(f"Failed {url}: {str(e)}")

    async def crawl(self):
        """Main crawling function"""
        urls = self.load_urls(r"C:\Users\Vivek\Documents\MikroTik_dis\urls.txt")
        
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            for i in range(0, len(urls), 2):
                batch = urls[i:i+2]
                tasks = [self.crawl_page(url, crawler) for url in batch]
                await asyncio.gather(*tasks)
                await asyncio.sleep(2)
                logging.info(f"Completed batch {i//2 + 1} of {(len(urls) + 1)//2}")

if __name__ == "__main__":
    crawler = MikroTikDocCrawler()
    asyncio.run(crawler.crawl())