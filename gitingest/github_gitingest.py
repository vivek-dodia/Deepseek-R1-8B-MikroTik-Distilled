import os
from pathlib import Path
from gitingest import ingest
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paths
INPUT_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\github_repos"
OUTPUT_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\github_repos"

# Files and directories to exclude from content
EXCLUDE_PATTERNS = [
    r'\.git/',
    r'__pycache__/',
    r'node_modules/',
    r'\.idea/',
    r'\.vscode/',
    r'\.DS_Store',
    r'\.pyc$',
    r'\.pyo$',
    r'\.pyd$',
    r'\.log$'
]

# Combine patterns into a single regex
EXCLUDE_REGEX = re.compile('|'.join(EXCLUDE_PATTERNS))

def clean_content(content: str) -> str:
    """Clean the content by removing unwanted sections."""
    # Split content into lines
    lines = content.split('\n')
    cleaned_lines = []
    skip_section = False
    
    for line in lines:
        # Check if line contains any excluded patterns
        if EXCLUDE_REGEX.search(line):
            skip_section = True
            continue
            
        # Reset skip_section flag on new file section
        if line.startswith('================================================'):
            skip_section = False
            continue
            
        # Skip lines in excluded sections
        if skip_section:
            continue
            
        # Keep relevant lines
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def clean_tree(tree: str) -> str:
    """Clean the directory tree by removing unwanted entries."""
    lines = tree.split('\n')
    return '\n'.join(line for line in lines 
                    if not EXCLUDE_REGEX.search(line))

def process_repos():
    """Process repositories and create clean markdown output."""
    
    # Create output directory if it doesn't exist
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    # Get list of repositories
    repos = [d for d in Path(INPUT_DIR).iterdir() if d.is_dir()]
    total_repos = len(repos)
    
    logging.info(f"Found {total_repos} repositories to process")
    
    # Process each repository
    for idx, repo_path in enumerate(repos, 1):
        try:
            logging.info(f"Processing {idx}/{total_repos}: {repo_path.name}")
            
            # Output file path
            output_file = Path(OUTPUT_DIR) / f"{repo_path.name}.md"
            
            # Process the repository using gitingest
            summary, tree, content = ingest(str(repo_path))
            
            # Clean up the content
            clean_tree_content = clean_tree(tree)
            clean_file_content = clean_content(content)
            
            # Format the output
            formatted_content = [
                "# Repository Information",
                f"Name: {repo_path.name}",
                "",
                "# Directory Structure",
                clean_tree_content,
                "",
                "# Content",
                clean_file_content
            ]
            
            # Write to file if there's meaningful content
            if len(clean_file_content.strip()) > 0:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(formatted_content))
                logging.info(f"Successfully processed {repo_path.name}")
            else:
                logging.info(f"Skipped {repo_path.name} - no relevant content")
            
        except Exception as e:
            logging.error(f"Error processing {repo_path.name}: {str(e)}")

if __name__ == "__main__":
    logging.info("Starting repository processing...")
    process_repos()
    logging.info("Processing complete!")