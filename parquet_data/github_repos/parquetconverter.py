import pandas as pd
from pathlib import Path
import re
import logging
from typing import Dict, List, Any
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MikroTikGitHubProcessor:
    def __init__(self):
        self.file_markers = {
            'start': 'File: ',
            'separator': '\n\n'
        }
        
        self.ignore_patterns = [
            r'\.git/',
            r'\.github/',
            r'LICENSE',
            r'\.gitignore',
            r'\.gitmodules',
            r'package-lock\.json',
            r'yarn\.lock'
        ]
        
        self.mikrotik_patterns = {
            'commands': [
                r'/ip\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/system\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/interface\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/routing\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/ppp\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/queue\s+[a-z-]+(?:\s+[a-z-]+)*',
                r'/tool\s+[a-z-]+(?:\s+[a-z-]+)*'
            ],
            'services': [
                'hotspot', 'firewall', 'dhcp', 'dns', 'ntp',
                'snmp', 'radius', 'web-proxy', 'pppoe', 'l2tp'
            ]
        }

    def should_process_file(self, filename: str) -> bool:
        """Check if file should be processed"""
        return not any(re.search(pattern, filename, re.IGNORECASE) 
                      for pattern in self.ignore_patterns)

    def extract_mikrotik_commands(self, content: str) -> List[str]:
        """Extract RouterOS commands from content"""
        commands = set()
        for pattern in self.mikrotik_patterns['commands']:
            matches = re.findall(pattern, content, re.IGNORECASE)
            commands.update(matches)
        return list(commands)

    def detect_config_type(self, content: str) -> str:
        """Detect type of MikroTik configuration"""
        config_patterns = {
            'firewall': r'firewall|nat|filter|mangle',
            'routing': r'routing|ospf|bgp|rip|static-route',
            'interface': r'interface|bridge|vlan|port|ethernet',
            'system': r'system|scheduler|script|user|resource',
            'monitoring': r'snmp|graphing|tool|traffic-monitor',
            'security': r'security|certificate|ssh|tls|encryption',
            'vpn': r'vpn|ipsec|l2tp|pptp|sstp|ovpn',
            'wireless': r'wireless|wifi|wlan|ap|station',
            'hotspot': r'hotspot|radius|user-manager|captive-portal',
            'qos': r'queue|qos|traffic-control|limitation'
        }
        
        matched_types = []
        for ctype, pattern in config_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                matched_types.append(ctype)
        
        return ','.join(matched_types) if matched_types else 'other'

    def extract_repo_metadata(self, content: str) -> Dict[str, str]:
        """Extract repository metadata"""
        patterns = {
            'description': r'# Project Information\s+(.+?)(?=\n#|\Z)',
            'author': r'Author\s*:\s*(.+?)(?=\n|$)',
            'version': r'version\s*:\s*(.+?)(?=\n|$)',
            'updated': r'updated\s*:\s*(.+?)(?=\n|$)',
            'cve': r'CVE\s*:\s*(.+?)(?=\n|$)',
            'license': r'License\s*:\s*(.+?)(?=\n|$)'
        }
        
        metadata = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                metadata[key] = match.group(1).strip()
        
        return metadata

    def extract_code_patterns(self, content: str) -> List[str]:
        """Extract common code patterns and implementations"""
        patterns = {
            'api_implementation': r'RouterOS\\Client|Net\\RouterOS',
            'backup_restore': r'system\s+backup|export\s+configuration',
            'monitoring_setup': r'snmp|health|traffic|tool\s+graphing',
            'automation': r'scheduler|script|automatic|cron',
            'security_config': r'firewall|filter|security|certificate',
            'vpn_setup': r'vpn|ipsec|l2tp|pptp|wireguard',
            'qos_config': r'queue\s+type|queue\s+tree|simple\s+queue',
            'hotspot_setup': r'hotspot|user\s+profile|walled-garden'
        }
        
        found_patterns = []
        for name, regex in patterns.items():
            if re.search(regex, content, re.IGNORECASE):
                found_patterns.append(name)
        
        return found_patterns

    def parse_md_file(self, file_path: Path) -> pd.DataFrame:
        """Parse a single markdown file containing repository data"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Extract repository name and metadata
            repo_name = file_path.stem
            metadata = self.extract_repo_metadata(content)
            
            # Split content into files
            files_data = []
            file_blocks = content.split('\nFile: ')
            
            for block in file_blocks[1:]:
                try:
                    filename = block.split('\n', 1)[0].strip()
                    
                    if not self.should_process_file(filename):
                        continue
                        
                    content_parts = block.split(self.file_markers['separator'])
                    if len(content_parts) > 1:
                        file_content = content_parts[1].strip()
                    else:
                        continue

                    file_data = {
                        'repo_name': repo_name,
                        'filename': filename,
                        'file_content': file_content,
                        'extension': Path(filename).suffix.lower(),
                        'content_length': len(file_content),
                        'line_count': len(file_content.split('\n')),
                        'commands_used': json.dumps(self.extract_mikrotik_commands(file_content)),
                        'config_type': self.detect_config_type(file_content),
                        'code_patterns': json.dumps(self.extract_code_patterns(file_content)),
                        'has_networking': bool(re.search(r'interface|ip|routing', file_content, re.IGNORECASE)),
                        'has_automation': bool(re.search(r'scheduler|script|auto', file_content, re.IGNORECASE)),
                        'has_security': bool(re.search(r'firewall|certificate|encryption', file_content, re.IGNORECASE)),
                        'is_config': any(ext in filename.lower() for ext in ['.conf', '.cfg', '.rsc', '.yml', '.yaml', '.json']),
                        'is_source': Path(filename).suffix.lower() in ['.py', '.js', '.php', '.sh', '.go', '.rb'],
                        'is_documentation': Path(filename).suffix.lower() in ['.md', '.txt', '.rst', '.doc'],
                        'repo_description': metadata.get('description', ''),
                        'repo_author': metadata.get('author', ''),
                        'repo_version': metadata.get('version', ''),
                        'repo_updated': metadata.get('updated', ''),
                        'repo_cve': metadata.get('cve', ''),
                        'repo_license': metadata.get('license', '')
                    }
                    
                    files_data.append(file_data)
                    
                except Exception as e:
                    logger.warning(f"Error processing file block in {filename}: {str(e)}")
                    continue
                    
            return pd.DataFrame(files_data)
            
        except Exception as e:
            logger.error(f"Error processing markdown file {file_path}: {str(e)}")
            return pd.DataFrame()

def process_github_repos(input_dir: str, output_file: str):
    """Process all markdown files in directory into a single dataset"""
    processor = MikroTikGitHubProcessor()
    all_data = []
    input_path = Path(input_dir)
    
    logger.info(f"Processing markdown files from: {input_dir}")
    
    # Process each markdown file
    for md_file in input_path.glob('*.md'):
        logger.info(f"Processing file: {md_file.name}")
        df = processor.parse_md_file(md_file)
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
    
    # Print statistics
    logger.info(f"\nDataset Creation Summary:")
    logger.info(f"Total repositories processed: {final_df['repo_name'].nunique()}")
    logger.info(f"Total files processed: {len(final_df)}")
    logger.info(f"Dataset saved to: {output_file}")
    
    logger.info("\nFile Statistics:")
    logger.info(f"Configuration files: {final_df['is_config'].sum()}")
    logger.info(f"Source code files: {final_df['is_source'].sum()}")
    logger.info(f"Documentation files: {final_df['is_documentation'].sum()}")
    
    logger.info("\nContent Statistics:")
    logger.info(f"Files with networking: {final_df['has_networking'].sum()}")
    logger.info(f"Files with automation: {final_df['has_automation'].sum()}")
    logger.info(f"Files with security: {final_df['has_security'].sum()}")
    
    config_types = final_df['config_type'].value_counts()
    logger.info("\nConfiguration Types:")
    for ctype, count in config_types.items():
        logger.info(f"{ctype}: {count}")

if __name__ == "__main__":
    input_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\github_repos"
    output_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\github_repos\github_dataset.parquet"
    
    process_github_repos(input_dir, output_file)