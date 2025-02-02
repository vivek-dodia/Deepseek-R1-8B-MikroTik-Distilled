import asyncio
import logging
from pathlib import Path
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("crawler.log"), logging.StreamHandler()]
)

def clean_github_markdown(content: str) -> str:
    """Clean raw GitHub content"""
    return content  # Raw GitHub files don't need cleaning

def clean_mikrotik_markdown(content: str) -> str:
    """MikroTik documentation cleaner"""
    cleaned = []
    keep = False
    for line in content.split('\n'):
        if "First Time Configuration" in line:
            keep = True
        if not keep:
            continue
        if any(kw in line for kw in ["Page tree", "breadcrumbs", "Attachments"]):
            continue
        cleaned.append(line)
    return '\n'.join(cleaned)

async def crawl_urls(urls: list):
    """Simplified crawler with maximum compatibility"""
    browser_config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig(word_count_threshold=50)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for url in urls:
            try:
                logging.info(f"Starting: {url}")
                result = await crawler.arun(url, config=run_config)
                
                if result.success:
                    domain = url.split("//")[-1].split("/")[0]
                    filename = f"Scraped_Data/{domain}_output.md"
                    
                    content = result.markdown
                    if "help.mikrotik.com" in url:
                        content = clean_mikrotik_markdown(content)
                    
                    Path(filename).write_text(content, encoding="utf-8")
                    logging.info(f"Saved: {filename}")
                
            except Exception as e:
                logging.error(f"Failed {url}: {str(e)}")

if __name__ == "__main__":
    Path("Scraped_Data").mkdir(exist_ok=True)
    
    # Test URLs
    TEST_URLS = [
        "https://help.mikrotik.com/docs/display/ROS/First+Time+Configuration",
        "https://raw.githubusercontent.com/ivanovnikita/routeros-scripts/main/scripts/bandwidth-monitor.rsc"
    ]
    
    asyncio.run(crawl_urls(TEST_URLS))