import os
from PyPDF2 import PdfReader
import re

def extract_and_format_md(pdf_path: str, output_path: str):
    """Extract and format content from a PDF file into Markdown.

    This function reads a PDF file specified by `pdf_path`, extracts the
    text from each page, and formats it into Markdown. It identifies headers
    based on specific patterns and organizes the content into sections. The
    formatted Markdown content is then written to a file specified by
    `output_path`. The function ensures that the output directory exists
    before writing the file.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_path (str): The path where the output Markdown file will be saved.
    """

    reader = PdfReader(pdf_path)
    current_section = ''
    md_content = []
    
    for page in reader.pages:
        text = page.extract_text()
        
        # Clean text
        text = re.sub(r'\s+', ' ', text)
        
        # Detect headers
        headers = re.finditer(r'(?m)^[A-Z][A-Za-z\s]{2,}(?:\n|$)', text)
        for match in headers:
            header = match.group().strip()
            if len(header.split()) <= 5:  # Avoid long sentences
                if header != current_section:
                    current_section = header
                    md_content.append(f"\n## {header}\n")
        
        # Process content
        paragraphs = re.split(r'\n\s*\n', text)
        for para in paragraphs:
            para = para.strip()
            if para and not para.startswith('#'):
                # Clean paragraph
                para = re.sub(r'^.*MikroTik.*\n?', '', para)
                para = re.sub(r'\b\d+\s*$', '', para)
                para = para.strip()
                if para:
                    md_content.append(para + "\n\n")
    
    # Write to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# MikroTik Documentation\n\n")
        f.write(''.join(md_content))

if __name__ == "__main__":
    pdf_path = r"C:\Users\Vivek\Documents\MikroTik_dis\PDF_Docs\ROS-100125-1421-5242.pdf"
    output_path = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\processed_pdf\documentation.md"
    extract_and_format_md(pdf_path, output_path)