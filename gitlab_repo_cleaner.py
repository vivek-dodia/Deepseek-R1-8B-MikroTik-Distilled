import os
from pathlib import Path
import re
import shutil
import hashlib
import logging
from typing import Set, Dict, List
import json

class MikroTikContentCleaner:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.file_hashes = {}  # Track file hashes to detect duplicates
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('mikrotik_content_cleaning.log'),
                logging.StreamHandler()
            ]
        )
        
        # Patterns to identify MikroTik-specific content
        self.mikrotik_patterns = {
            'config': ['.rsc', '.conf', '.backup'],
            'script': ['.py', '.sh', '.js', '.php'],
            'documentation': ['.md', '.txt'],
        }
        
        # Important file patterns
        self.important_patterns = [
            r'routeros',
            r'mikrotik',
            r'winbox',
            r'ros\b',
            r'\/ip\b',
            r'\/interface\b',
            r'\/system\b',
            r'\/tool\b'
        ]
        
        # Categories for organizing content
        self.categories = {
            'networking': [
                'interface', 'bridge', 'vlan', 'routing', 'firewall', 
                'nat', 'dhcp', 'dns', 'vpn', 'wireless'
            ],
            'security': [
                'firewall', 'certificate', 'ipsec', 'authentication',
                'encryption', 'radius'
            ],
            'automation': [
                'script', 'scheduler', 'backup', 'monitoring', 'api'
            ],
            'management': [
                'user', 'group', 'password', 'identity', 'logging'
            ]
        }

    def get_file_hash(self, file_path: Path) -> str:
        """Calculate hash of file content to identify duplicates."""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def is_mikrotik_related(self, file_path: Path, content: str) -> bool:
        """Check if file content is MikroTik-related."""
        # Check filename patterns
        if any(file_path.name.lower().find(pattern) != -1 
               for pattern in ['mikrotik', 'routeros', 'ros', 'winbox']):
            return True
            
        # Check content patterns
        return any(re.search(pattern, content, re.IGNORECASE) 
                  for pattern in self.important_patterns)

    def categorize_content(self, content: str) -> List[str]:
        """Determine categories for the content."""
        categories = []
        for category, keywords in self.categories.items():
            if any(keyword in content.lower() for keyword in keywords):
                categories.append(category)
        return categories or ['uncategorized']

    def clean_and_organize_content(self):
        """Main function to clean and organize MikroTik content."""
        processed_files = 0
        duplicate_files = 0
        organized_files = 0

        # Create output directory structure
        for category in self.categories.keys():
            (self.output_dir / category).mkdir(parents=True, exist_ok=True)

        # Process each repository
        for repo_dir in self.input_dir.iterdir():
            if not repo_dir.is_dir():
                continue

            logging.info(f"Processing repository: {repo_dir.name}")

            try:
                # Process files in repository
                for file_path in repo_dir.rglob('*'):
                    if not file_path.is_file():
                        continue

                    processed_files += 1
                    
                    try:
                        # Read file content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Skip if not MikroTik related
                        if not self.is_mikrotik_related(file_path, content):
                            continue

                        # Check for duplicates
                        file_hash = self.get_file_hash(file_path)
                        if file_hash in self.file_hashes:
                            duplicate_files += 1
                            continue
                        self.file_hashes[file_hash] = file_path

                        # Determine categories
                        categories = self.categorize_content(content)
                        
                        # Save file in appropriate categories
                        for category in categories:
                            output_path = self.output_dir / category / f"{repo_dir.name}_{file_path.name}"
                            shutil.copy2(file_path, output_path)
                            organized_files += 1

                    except Exception as e:
                        logging.error(f"Error processing file {file_path}: {str(e)}")

            except Exception as e:
                logging.error(f"Error processing repository {repo_dir}: {str(e)}")

        # Generate summary
        summary = {
            'processed_files': processed_files,
            'duplicate_files': duplicate_files,
            'organized_files': organized_files,
            'categories': {cat: len(list((self.output_dir / cat).glob('*'))) 
                         for cat in self.categories.keys()}
        }

        # Save summary
        with open(self.output_dir / 'cleaning_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)

        logging.info("\nCleaning Summary:")
        logging.info(f"Total files processed: {processed_files}")
        logging.info(f"Duplicate files skipped: {duplicate_files}")
        logging.info(f"Files organized: {organized_files}")
        for category, count in summary['categories'].items():
            logging.info(f"{category}: {count} files")

if __name__ == "__main__":
    input_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\gitlab_repos"
    output_directory = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\gitlab_repos"
    
    cleaner = MikroTikContentCleaner(input_directory, output_directory)
    cleaner.clean_and_organize_content()