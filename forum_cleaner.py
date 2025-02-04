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
    # Remove "Code:Select all" prefix but keep the code
    text = re.sub(r'Code:Select\s*all\s*', '', text)
    text = text.strip()
    
    # If not already in code blocks, wrap it
    if not text.startswith('```') and text.strip():
        text = f'```\n{text}\n```'
    
    return text

def clean_text(text: str) -> str:
    """Clean general text content while preserving structure."""
    if not text:
        return ""
    
    # Preserve code blocks
    code_blocks = []
    
    def save_code_block(match):
        code = match.group(1).strip()
        if code:
            code_blocks.append(code)
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"
        return ""
    
    # Extract code blocks
    pattern = r'Code:Select\s*all(.*?)(?=Code:Select\s*all|$)'
    text = re.sub(pattern, save_code_block, text, flags=re.DOTALL)
    
    # Basic text cleaning
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(?<=\w),(?=\w)', ', ', text)
    text = text.strip()
    
    # Restore code blocks
    for i, block in enumerate(code_blocks):
        text = text.replace(f"__CODE_BLOCK_{i}__", clean_code_blocks(block))
    
    return text

def parse_post(post_text: str) -> Optional[Post]:
    """Parse individual post content."""
    try:
        # Extract post number from the ### Post X format
        post_num_match = re.search(r'### Post (\d+)', post_text)
        if not post_num_match:
            return None
        
        post_number = int(post_num_match.group(1))
        
        # Split the remaining content
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
            post_number=post_number
        )
    except Exception as e:
        logging.error(f"Error parsing post: {str(e)}")
        return None

def parse_thread(thread_text: str) -> Optional[Thread]:
    """Parse complete thread content."""
    try:
        # Extract metadata section between the first two '---' marks
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
        
        # Split posts using ### Post marker
        post_texts = re.split(r'### Post \d+', posts_text)
        post_numbers = re.findall(r'### Post (\d+)', posts_text)
        
        posts = []
        for i, (post_text, post_num) in enumerate(zip(post_texts[1:], post_numbers)):
            full_post = f"### Post {post_num}\n{post_text.strip()}"
            post = parse_post(full_post)
            if post:
                posts.append(post)
        
        return Thread(
            title=metadata.get('title', ''),
            url=metadata.get('url', ''),
            thread_id=metadata.get('thread_id', ''),
            section=metadata.get('section', ''),
            post_count=int(metadata.get('post_count', 0)),
            date_crawled=metadata.get('date_crawled', ''),
            posts=posts
        )
    except Exception as e:
        logging.error(f"Error parsing thread: {str(e)}")
        return None

def format_thread_for_training(thread: Thread) -> str:
    """Format thread for training, preserving chain of thought."""
    output = []
    
    # Add thread metadata
    output.append("---")
    output.append(f"Title: {thread.title}")
    output.append(f"Section: {thread.section}")
    output.append(f"Thread ID: {thread.thread_id}")
    output.append(f"URL: {thread.url}")
    output.append("---")
    output.append("")
    
    # Process posts sequentially
    for post in thread.posts:
        output.append(f"### Post {post.post_number}")
        output.append(f"Author: {post.author}")
        output.append(f"Date: {post.date}")
        output.append("")
        output.append(post.content)
        output.append("")
        output.append("---")
        output.append("")
    
    return "\n".join(output)

def process_directory(input_dir: str, output_dir: str):
    """Process all .md files in the input directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Initialize counters
    total_files = 0
    successful_files = 0
    failed_files = 0
    
    # Process each .md file
    for md_file in input_path.glob('**/*.md'):
        total_files += 1
        try:
            # Read the input file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Process the thread
            thread = parse_thread(content)
            if thread and thread.posts:
                # Create the output filename
                output_file = output_path / f"cleaned_{md_file.name}"
                
                # Format and save the thread
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
    
    # Log summary
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