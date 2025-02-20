import os
from PyPDF2 import PdfReader
import re

def clean_text(text: str) -> str:
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def is_code_block(text: str) -> bool:
    patterns = [
        r'^\[.+?\].+?>.*$',  # Command prompts
        r'^#\s+NAME\s+\w+.*$',  # Table headers
        r'^\d+\s+\w+\s+\d+.*$',  # Numbered outputs
        r'^Flags:.*$',  # Flag definitions
    ]
    return any(re.match(pattern, text) for pattern in patterns)

def extract_and_format_md(pdf_path: str, output_path: str):
    reader = PdfReader(pdf_path)
    md_content = []
    in_code_block = False
    content_buffer = []
    
    def flush_buffer():
        if content_buffer:
            md_content.append(' '.join(content_buffer) + '\n\n')
            content_buffer.clear()
    
    for page in reader.pages:
        text = page.extract_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Handle headers
            if line.startswith('#'):
                flush_buffer()
                md_content.append(f"{line}\n\n")
                continue
            
            # Handle code blocks
            if is_code_block(line):
                if not in_code_block:
                    flush_buffer()
                    md_content.append("```\n")
                    in_code_block = True
                md_content.append(f"{line}\n")
            else:
                if in_code_block:
                    md_content.append("```\n\n")
                    in_code_block = False
                content_buffer.append(clean_text(line))
    
    # Clean up any remaining content
    if in_code_block:
        md_content.append("```\n\n")
    flush_buffer()

    # Write to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(md_content))

if __name__ == "__main__":
    pdf_path = r"C:\Users\Vivek\Documents\MikroTik_dis\PDF_Docs\ROS-100125-1421-5242.pdf"
    output_path = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\processed_pdf\ros_documentation.md"
    extract_and_format_md(pdf_path, output_path)