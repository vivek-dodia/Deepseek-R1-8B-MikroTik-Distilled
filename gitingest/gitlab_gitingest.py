import os
from pathlib import Path
from gitingest import ingest
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INPUT_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\gitlab_repos"
OUTPUT_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\gitlab_repos"

EXCLUDE_PATTERNS = [
    r'\.git/', r'__pycache__/', r'node_modules/', r'\.idea/',
    r'\.vscode/', r'\.DS_Store', r'\.(pyc|pyo|pyd|log)$'
]

RELEVANT_EXTENSIONS = {
    '.py', '.sh', '.conf', '.rsc', '.txt', '.md', '.yml', '.yaml',
    '.json', '.html', '.js', '.css'
}

RELEVANT_FILENAMES = {
    'README', 'LICENSE', 'Dockerfile', 'requirements.txt',
    '.gitlab-ci.yml', 'config.conf'
}

RELEVANT_KEYWORDS = {
    'mikrotik', 'routeros', 'winbox', 'api', 'router', 
    'network', 'script', 'config'
}

def get_file_url(content: str) -> str:
    match = re.search(r'url = (.+)\.git', content)
    return match.group(1) if match else ""

def is_relevant_file(filepath: str) -> bool:
    path = Path(filepath)
    return (path.suffix.lower() in RELEVANT_EXTENSIONS or
            path.stem in RELEVANT_FILENAMES or
            any(k in path.name.lower() for k in RELEVANT_KEYWORDS))

def clean_content(content: str) -> str:
    lines = content.split('\n')
    cleaned_lines = []
    current_file = ''
    include_section = False
    repo_url = ""
    
    for line in lines:
        if line.startswith('File: '):
            current_file = line[6:].strip()
            if '.git/config' in current_file:
                repo_url = get_file_url(content)
            include_section = is_relevant_file(current_file)
            if include_section:
                cleaned_lines.append(f"\nFile: {Path(current_file).name}")
        elif include_section and line.strip():
            cleaned_lines.append(line)
            
    return '\n'.join(cleaned_lines).strip(), repo_url

def clean_tree(tree: str) -> str:
    return '\n'.join(line for line in tree.split('\n') 
                    if any(ext in line for ext in RELEVANT_EXTENSIONS) or
                    any(name in line for name in RELEVANT_FILENAMES))

def format_repo_info(name: str, url: str, description: str = "") -> str:
    info = [
        "# Repository Information",
        f"Name: {name}",
        f"URL: {url}" if url else "",
        f"Description: {description}" if description else "",
        "\n# Files",
    ]
    return '\n'.join(line for line in info if line)

def process_repos():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    repos = [d for d in Path(INPUT_DIR).iterdir() if d.is_dir()]
    
    for idx, repo_path in enumerate(repos, 1):
        try:
            logging.info(f"Processing {idx}/{len(repos)}: {repo_path.name}")
            output_file = Path(OUTPUT_DIR) / f"{repo_path.name}.md"
            
            summary, tree, content = ingest(str(repo_path))
            clean_file_content, repo_url = clean_content(content)
            
            if clean_file_content:
                formatted_content = [
                    format_repo_info(repo_path.name, repo_url),
                    clean_file_content
                ]
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(formatted_content))
                logging.info(f"Processed {repo_path.name}")
                
        except Exception as e:
            logging.error(f"Error processing {repo_path.name}: {str(e)}")

def format_repo_info(name: str, url: str) -> str:
    info = [
        "# Repository Information",
        f"Name: {name}",
        f"URL: {url}" if url else "",
        "\n# Files",
    ]
    return '\n'.join(line for line in info if line)

if __name__ == "__main__":
    process_repos()