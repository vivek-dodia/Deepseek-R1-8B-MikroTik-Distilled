import re
from dataclasses import dataclass
from typing import List, Optional
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('forum_cleaner_detailed.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Post:
    content: str
    author: str
    date: str
    post_number: int

@dataclass
class Thread:
    title: str
    url: str
    thread_id: str
    section: str
    post_count: int
    date_crawled: str
    posts: List[Post]

def clean_code_blocks(text: str) -> str:
    """Clean up code blocks while preserving structure."""
    # Remove "Code:Select all" prefix
    text = re.sub(r'Code:Select\s*all\s*', '', text)
    # Remove empty code blocks
    if not text.strip():
        return ""
    # Ensure proper code block formatting
    text = text.strip()
    if not text.startswith('```'):
        text = f'```\n{text}\n```'
    return text

def clean_text(text: str) -> str:
    """Clean general text content while preserving structure."""
    if not text:
        return ""
    
    # Extract and save code blocks
    code_blocks = []
    
    def save_code_block(match):
        code = match.group(1).strip()
        if code:
            code_blocks.append(code)
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        return ""
    
    # Handle Code:Select all blocks
    pattern = r'Code:Select\s*all(.*?)(?=Code:Select\s*all|$)'
    text = re.sub(pattern, save_code_block, text, flags=re.DOTALL)
    
    # Clean the main text
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'(?<=\w),(?=\w)', ', ', text)  # Add space after commas
    text = text.strip()
    
    # Restore code blocks with proper formatting
    for i, block in enumerate(code_blocks):
        cleaned_block = clean_code_blocks(block)
        if cleaned_block:
            text = text.replace(f"__CODE_BLOCK_{i}__", f"\n{cleaned_block}\n")
    
    return text

def parse_post_format1(post_text: str, post_num: int) -> Optional[Post]:
    """Parse post with '### Post X' format."""
    try:
        lines = post_text.split('\n')
        author = "Unknown"
        date = "Unknown"
        content_lines = []
        content_started = False
        
        for line in lines:
            if line.startswith('Author:'):
                author = line.replace('Author:', '').strip()
            elif line.startswith('Date:'):
                date = line.replace('Date:', '').strip()
            elif content_started:
                content_lines.append(line)
            elif line.strip() == '':
                content_started = True
        
        content = '\n'.join(content_lines).strip()
        content = clean_text(content)
        
        return Post(
            content=content,
            author=author,
            date=date,
            post_number=post_num
        )
    except Exception as e:
        logging.error(f"Error parsing post format 1: {str(e)}")
        return None

def parse_post_format2(post_text: str, post_num: int) -> Optional[Post]:
    """Parse post with '### Author:' format."""
    try:
        lines = post_text.split('\n')
        author = "Unknown"
        date = "Unknown"
        content_lines = []
        content_started = False
        
        # Extract author from first line
        if lines[0].startswith('### Author:'):
            author = lines[0].replace('### Author:', '').strip()
            
        # Process remaining lines
        for line in lines[1:]:
            if line.startswith('Date:'):
                date = line.replace('Date:', '').strip()
            elif content_started:
                content_lines.append(line)
            elif line.strip() == '':
                content_started = True
        
        content = '\n'.join(content_lines).strip()
        content = clean_text(content)
        
        return Post(
            content=content,
            author=author,
            date=date,
            post_number=post_num
        )
    except Exception as e:
        logging.error(f"Error parsing post format 2: {str(e)}")
        return None

def parse_thread(thread_text: str) -> Optional[Thread]:
    """Parse complete thread content."""
    try:
        # Extract metadata section
        parts = thread_text.split('---', 2)
        if len(parts) < 3:
            return None
            
        meta_text = parts[1].strip()
        posts_text = parts[2].strip()
        
        # Parse metadata
        metadata = {}
        for line in meta_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        # Determine thread format and parse posts accordingly
        posts = []
        post_num = 1
        
        if '### Post' in posts_text:
            # Format 1: "### Post X"
            post_texts = re.split(r'### Post \d+', posts_text)
            post_numbers = re.findall(r'### Post (\d+)', posts_text)
            
            for i, (post_text, num) in enumerate(zip(post_texts[1:], post_numbers)):
                full_post = f"### Post {num}\n{post_text.strip()}"
                post = parse_post_format1(full_post, int(num))
                if post:
                    posts.append(post)
        else:
            # Format 2: "### Author:"
            post_texts = re.split(r'### Author:', posts_text)
            for i, post_text in enumerate(post_texts[1:], 1):
                post = parse_post_format2(f"### Author:{post_text.strip()}", i)
                if post:
                    posts.append(post)
        
        # Get thread ID from metadata or URL
        thread_id = metadata.get('thread_id', '')
        if not thread_id and 'source_url' in metadata:
            url_match = re.search(r't=(\d+)', metadata['source_url'])
            if url_match:
                thread_id = url_match.group(1)
        
        return Thread(
            title=metadata.get('title', ''),
            url=metadata.get('source_url', metadata.get('url', '')),
            thread_id=thread_id,
            section=metadata.get('section', ''),
            post_count=len(posts),
            date_crawled=metadata.get('crawled_date', metadata.get('date_crawled', '')),
            posts=posts
        )
    except Exception as e:
        logging.error(f"Error parsing thread: {str(e)}")
        return None

def format_thread_for_training(thread: Thread) -> str:
    """Format thread for training, preserving chain of thought."""
    output = []
    
    # Thread header
    output.append("# Thread Information")
    output.append(f"Title: {thread.title}")
    output.append(f"Section: {thread.section}")
    output.append(f"Thread ID: {thread.thread_id}")
    output.append("")
    
    # Posts
    output.append("# Discussion")
    for i, post in enumerate(thread.posts):
        # Format post header
        if i == 0:
            output.append("\n## Initial Question")
        else:
            output.append(f"\n## Response {i}")
        
        # Add post metadata
        if post.author != "Unknown":
            output.append(f"Author: {post.author}")
        
        # Add post content
        content = post.content.strip()
        output.append(content)
    
    return "\n".join(output)

def process_directory(input_dir: str, output_dir: str):
    """Process all .md files in the input directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    total_files = 0
    successful_files = 0
    failed_files = 0
    
    for md_file in input_path.glob('**/*.md'):
        total_files += 1
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            thread = parse_thread(content)
            if thread and thread.posts:
                output_file = output_path / f"cleaned_{md_file.name}"
                formatted_content = format_thread_for_training(thread)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(formatted_content)
                
                successful_files += 1
                if successful_files % 100 == 0:
                    logging.info(f"Processed {successful_files} files successfully...")
            else:
                failed_files += 1
                logging.error(f"Failed to parse thread content in: {md_file.name}")
        except Exception as e:
            failed_files += 1
            logging.error(f"Error processing {md_file.name}: {str(e)}")
    
    logging.info("\nProcessing Summary:")
    logging.info(f"Total files processed: {total_files}")
    logging.info(f"Successfully cleaned: {successful_files}")
    logging.info(f"Failed to process: {failed_files}")
    
    return successful_files, failed_files

if __name__ == "__main__":
    input_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\forum"
    output_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\forum"
    
    logging.info("Starting forum thread cleaning process...")
    successful, failed = process_directory(input_directory, output_directory)
    logging.info("Cleaning process completed!")