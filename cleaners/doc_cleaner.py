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
        logging.FileHandler('docs_cleaner.log'),
        logging.StreamHandler()
    ]
)

@dataclass
class Document:
    title: str
    section: str
    url: str
    content: str
    date_crawled: str

def clean_code_blocks(text: str) -> str:
    """Clean up code blocks while preserving structure."""
    # Remove empty code blocks
    if not text.strip():
        return ""
    
    # Ensure proper code block formatting
    text = text.strip()
    if not text.startswith('```'):
        text = f'```\n{text}\n```'
    return text

def clean_list_items(text: str) -> str:
    """Clean up list items and ensure proper formatting."""
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Handle bullet points
        line = re.sub(r'^\*\s+', '* ', line.strip())
        # Handle numbered lists
        line = re.sub(r'^\d+\.\s+', '1. ', line.strip())
        if line:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

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
    
    # Handle code blocks
    pattern = r'```(.*?)```'
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

def parse_document(doc_text: str) -> Optional[Document]:
    """Parse complete document content."""
    try:
        # Extract metadata section
        parts = doc_text.split('---', 2)
        if len(parts) < 3:
            return None
            
        meta_text = parts[1].strip()
        content_text = parts[2].strip()
        
        # Parse metadata
        metadata = {}
        for line in meta_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        # Remove redundant table of contents lists at the start
        content_text = re.sub(r'^\s*\*[^\n]*\n+', '', content_text, flags=re.MULTILINE)
        
        # Clean up section headers
        content_text = re.sub(r'#+\s*', '# ', content_text)
        
        # Clean up list items
        content_text = clean_list_items(content_text)
        
        return Document(
            title=metadata.get('title', ''),
            section=metadata.get('section', ''),
            url=metadata.get('source_url', ''),
            date_crawled=metadata.get('crawled_date', ''),
            content=content_text
        )
    except Exception as e:
        logging.error(f"Error parsing document: {str(e)}")
        return None

def format_document_for_training(doc: Document) -> str:
    """Format document for training, preserving structure."""
    output = []
    
    # Document header
    output.append("# Document Information")
    output.append(f"Title: {doc.title}")
    output.append(f"Section: {doc.section}")
    if doc.url:
        output.append(f"Source: {doc.url}")
    output.append("")
    
    # Content
    output.append("# Content")
    output.append(doc.content)
    
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
            
            doc = parse_document(content)
            if doc:
                output_file = output_path / f"cleaned_{md_file.name}"
                formatted_content = format_document_for_training(doc)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(formatted_content)
                
                successful_files += 1
                if successful_files % 100 == 0:
                    logging.info(f"Processed {successful_files} files successfully...")
            else:
                failed_files += 1
                logging.error(f"Failed to parse document content in: {md_file.name}")
        except Exception as e:
            failed_files += 1
            logging.error(f"Error processing {md_file.name}: {str(e)}")
    
    logging.info("\nProcessing Summary:")
    logging.info(f"Total files processed: {total_files}")
    logging.info(f"Successfully cleaned: {successful_files}")
    logging.info(f"Failed to process: {failed_files}")
    
    return successful_files, failed_files

if __name__ == "__main__":
    input_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\mikrotik_docs"
    output_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\mikrotik_docs"
    
    logging.info("Starting documentation cleaning process...")
    successful, failed = process_directory(input_directory, output_directory)
    logging.info("Cleaning process completed!")