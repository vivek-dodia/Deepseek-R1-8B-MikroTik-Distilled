import pandas as pd
from pathlib import Path
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MikroTikDatasetBuilder:
    def __init__(self):
        self.file_markers = {
            'start': 'File: ',
            'separator': '================================================'
        }
    
    def extract_mikrotik_commands(self, content):
        """Extract RouterOS commands from content"""
        command_patterns = [
            r'/ip\s+[a-z-]+(?:\s+[a-z-]+)*',
            r'/system\s+[a-z-]+(?:\s+[a-z-]+)*', 
            r'/interface\s+[a-z-]+(?:\s+[a-z-]+)*',
            r'/routing\s+[a-z-]+(?:\s+[a-z-]+)*'
        ]
        commands = []
        for pattern in command_patterns:
            commands.extend(re.findall(pattern, content, re.IGNORECASE))
        return list(set(commands))

    def detect_config_type(self, content):
        """Detect type of MikroTik configuration"""
        config_types = {
            'firewall': r'firewall|nat|filter|mangle',
            'routing': r'routing|ospf|bgp|rip',
            'interface': r'interface|bridge|vlan|port',
            'system': r'system|scheduler|script|user',
            'monitoring': r'snmp|graphing|tool'
        }
        
        for ctype, pattern in config_types.items():
            if re.search(pattern, content, re.IGNORECASE):
                return ctype
        return 'other'

    def extract_code_patterns(self, content):
        """Extract common code patterns and implementations"""
        return [pattern for pattern, regex in {
            'api_client': r'RouterOS\\Client|Net\\RouterOS',
            'config_backup': r'system\s+backup|export',
            'monitoring': r'snmp|health|traffic',
            'automation': r'scheduler|script|auto',
            'security': r'firewall|filter|security'
        }.items() if re.search(regex, content, re.IGNORECASE)]

    def parse_md_file(self, file_path):
        """Parse a single markdown file containing repository data"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Extract repository name
            repo_name_match = re.search(r'Name:\s*(.+?)(?:\n|$)', content)
            repo_name = repo_name_match.group(1).strip() if repo_name_match else Path(file_path).stem

            # Split content into files
            files_data = []
            file_blocks = content.split('\nFile: ')
            
            # Process each file block
            for block in file_blocks[1:]:  # Skip the first block (repo info)
                try:
                    # Split into filename and content
                    filename = block.split('\n', 1)[0].strip()
                    content_parts = block.split(self.file_markers['separator'])
                    if len(content_parts) > 1:
                        file_content = content_parts[1].strip()
                    else:
                        continue
                        
                    file_data = {
                        'repo_id': repo_name,
                        'repo_name': repo_name,
                        'file_id': f"{repo_name}_{filename}",
                        'filename': filename,
                        'extension': Path(filename).suffix.lower(),
                        'file_content': file_content,
                        'content_length': len(file_content),
                        'line_count': len(file_content.split('\n')),
                        'mikrotik_commands': self.extract_mikrotik_commands(file_content),
                        'config_type': self.detect_config_type(file_content),
                        'code_patterns': self.extract_code_patterns(file_content),
                        'has_networking': bool(re.search(r'interface|ip|routing', file_content, re.IGNORECASE)),
                        'has_automation': bool(re.search(r'scheduler|script|auto', file_content, re.IGNORECASE)),
                        'is_config': any(name in filename.lower() for name in ['config', 'settings', '.yml', '.json']),
                        'is_source': Path(filename).suffix.lower() in ['.py', '.js', '.cs', '.cpp', '.java', '.go', '.rs'],
                        'is_documentation': Path(filename).suffix.lower() in ['.md', '.txt', '.rst', '.doc']
                    }
                    
                    files_data.append(file_data)
                except Exception as e:
                    logger.error(f"Error processing file block in {file_path}: {str(e)}")
                    continue
                    
            return pd.DataFrame(files_data)
            
        except Exception as e:
            logger.error(f"Error processing markdown file {file_path}: {str(e)}")
            return pd.DataFrame()

def process_directory(input_dir, output_file):
    """Process all markdown files in directory into a single dataset"""
    builder = MikroTikDatasetBuilder()
    all_data = []
    input_path = Path(input_dir)
    
    logger.info(f"Processing markdown files from: {input_dir}")
    
    # Process each markdown file
    for md_file in input_path.glob('*.md'):
        logger.info(f"Processing file: {md_file.name}")
        df = builder.parse_md_file(md_file)
        if not df.empty:
            all_data.append(df)
            logger.info(f"Successfully processed {md_file.name} - Found {len(df)} files")
    
    if not all_data:
        logger.error("No data was processed. Check if input directory contains .md files")
        return
        
    # Combine all data
    final_df = pd.concat(all_data, ignore_index=True)
    
    # Create output directory if it doesn't exist
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to parquet
    final_df.to_parquet(output_file, index=False)
    
    logger.info(f"\nDataset creation completed:")
    logger.info(f"Total repositories processed: {final_df['repo_id'].nunique()}")
    logger.info(f"Total files processed: {len(final_df)}")
    logger.info(f"Dataset saved to: {output_file}")
    
    # Print some statistics
    logger.info("\nDataset Statistics:")
    logger.info(f"File types: {final_df['extension'].value_counts().to_dict()}")
    logger.info(f"Config types: {final_df['config_type'].value_counts().to_dict()}")
    logger.info(f"Average files per repo: {len(final_df) / final_df['repo_id'].nunique():.2f}")

if __name__ == "__main__":
    input_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\gitlab_repos"
    output_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\mikrotik_dataset.parquet"
    
    process_directory(input_dir, output_file)