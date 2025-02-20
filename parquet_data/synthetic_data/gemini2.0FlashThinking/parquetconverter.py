import os
import yaml
import re
import json
from typing import Dict, List
import pandas as pd
from datetime import datetime

def extract_frontmatter(content: str) -> Dict:
    """Extract and parse YAML frontmatter from markdown content.

    This function searches for YAML frontmatter enclosed within triple
    dashes at the beginning of the provided markdown content. If found, it
    attempts to parse the frontmatter using the `yaml.safe_load` method. If
    the frontmatter is not found or if there is an error during parsing, an
    empty dictionary is returned.

    Args:
        content (str): The markdown content from which to extract the frontmatter.

    Returns:
        Dict: A dictionary containing the parsed YAML frontmatter, or an empty
        dictionary if no frontmatter is found or if parsing fails.
    """
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return {}
    try:
        return yaml.safe_load(frontmatter_match.group(1))
    except yaml.YAMLError:
        return {}

def extract_code_blocks(content: str) -> List[Dict[str, str]]:
    """Extract code blocks with their language.

    This function scans the provided content for code blocks enclosed in
    triple backticks (```). It captures the programming language specified
    immediately after the opening backticks and the code contained within
    the block. The extracted code blocks are returned as a list of
    dictionaries, each containing the language and the corresponding code.

    Args:
        content (str): The input string containing code blocks.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each with 'language'
        and 'code' keys representing the programming language and the
        extracted code, respectively.
    """
    code_blocks = []
    pattern = r'```(\w*)\n(.*?)```'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        language = match.group(1) or 'text'
        code = match.group(2).strip()
        code_blocks.append({
            'language': language,
            'code': code
        })
    
    return code_blocks

def process_section_content(content: str) -> Dict:
    """Process section content to extract code blocks and clean content.

    This function takes a string containing section content, extracts any
    code blocks enclosed in triple backticks, and removes those code blocks
    from the main content. It returns a dictionary containing the cleaned
    content and a list of extracted code blocks.

    Args:
        content (str): The section content as a string, which may contain code blocks.

    Returns:
        Dict: A dictionary with two keys:
            - 'content': The cleaned content without code blocks.
            - 'code_blocks': A list of extracted code blocks.
    """
    code_blocks = extract_code_blocks(content)
    # Remove code blocks from main content
    clean_content = re.sub(r'```.*?```', '', content, flags=re.DOTALL).strip()
    
    return {
        'content': clean_content,
        'code_blocks': code_blocks
    }

def extract_sections(content: str) -> Dict[str, Dict]:
    """Extract sections and their subsections with structured content.

    This function processes a given string content to extract main sections
    and their corresponding subsections. It removes any frontmatter and
    organizes the content into a structured dictionary format. Each main
    section is identified by a '## ' prefix, while subsections are marked
    with a '### ' prefix. The function also processes the content of each
    section and subsection to ensure it is appropriately formatted.

    Args:
        content (str): The input string containing the content with sections
            and subsections.

    Returns:
        Dict[str, Dict]: A dictionary where keys are section titles and
            values are dictionaries containing 'main_content'
            and 'subsections'.
    """
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    sections = {}
    current_section = None
    current_subsections = {}
    
    # Split into main sections
    main_sections = re.split(r'(?=## )', content)
    
    for section in main_sections:
        if not section.strip():
            continue
        
        lines = section.split('\n')
        section_title = lines[0].replace('## ', '').strip()
        section_content = '\n'.join(lines[1:])
        
        # Process subsections
        subsections = {}
        subsection_splits = re.split(r'(?=### )', section_content)
        
        main_content = process_section_content(
            subsection_splits[0] if not subsection_splits[0].startswith('### ') else ''
        )
        
        for subsection in subsection_splits:
            if subsection.startswith('### '):
                sub_lines = subsection.split('\n')
                sub_title = sub_lines[0].replace('### ', '').strip()
                sub_content = '\n'.join(sub_lines[1:])
                subsections[sub_title] = process_section_content(sub_content)
        
        # Store section data
        sections[section_title] = {
            'main_content': main_content,
            'subsections': subsections
        }
    
    return sections

def process_markdown_for_dataset(input_dir: str, output_dir: str):
    """Process markdown files into a compact dataset structure.

    This function reads markdown files from the specified input directory,
    extracts relevant information from each file, and organizes it into a
    structured dataset. The extracted data includes metadata from the
    frontmatter of the markdown files and content from various sections. The
    resulting dataset is saved in a specified output directory in both YAML
    and Parquet formats.

    Args:
        input_dir (str): The directory containing markdown files to be processed.
        output_dir (str): The directory where the processed dataset will be saved.

    Returns:
        pandas.DataFrame: A DataFrame containing the processed dataset with extracted
        information from the markdown files.
    """
    
    os.makedirs(output_dir, exist_ok=True)
    dataset_rows = []
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(input_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract components
            frontmatter = extract_frontmatter(content)
            sections = extract_sections(content)
            
            # Create primary columns with cleaner names
            row_data = {
                'filename': filename,
                'timestamp': frontmatter.get('generated_at', ''),
                'prompt': frontmatter.get('topic', ''),
                'category': frontmatter.get('category', ''),
                'version': frontmatter.get('version', ''),
                'scale': frontmatter.get('scale', ''),
                'level': frontmatter.get('level', ''),
                'model': frontmatter.get('model', ''),
                'all_sections': json.dumps(sections)  # Complete content in JSON
            }
            
            # Extract common sections with clean names
            section_mapping = {
                'Introduction': 'intro',
                'CLI Configuration': 'cli_config',
                'API Configuration': 'api_config',
                'Examples': 'examples',
                'Security': 'security',
                'Troubleshooting': 'troubleshooting',
                'Architecture': 'architecture',
                'Validation': 'validation',
                'Performance': 'performance',
                'Monitoring': 'monitoring'
            }
            
            for original_name, clean_name in section_mapping.items():
                if original_name in sections:
                    row_data[clean_name] = json.dumps(sections[original_name])
            
            dataset_rows.append(row_data)
    
    # Create DataFrame
    df = pd.DataFrame(dataset_rows)
    
    # Add metadata
    metadata = {
        'name': 'mikrotik_routeros_docs',
        'version': '1.0.0',
        'created_at': datetime.now().isoformat(),
        'description': 'MikroTik RouterOS documentation dataset generated from synthetic data',
        'source': 'Generated using Gemini 2.0 Flash model',
        'license': 'MIT',
        'total_documents': len(df)
    }
    
    # Save metadata
    with open(os.path.join(output_dir, 'dataset_metadata.yaml'), 'w') as f:
        yaml.dump(metadata, f)
    
    # Export to parquet
    output_file = os.path.join(output_dir, 'mikrotik_routeros_docs.parquet')
    df.to_parquet(output_file, compression='snappy', index=False)
    
    print(f"\nDataset Summary:")
    print(f"Total files processed: {len(df)}")
    print(f"Categories covered: {df['category'].unique().tolist()}")
    print(f"Versions covered: {df['version'].unique().tolist()}")
    print(f"\nColumns in dataset:")
    for col in df.columns:
        print(f"- {col}")
    print(f"\nParquet file saved to: {output_file}")
    
    return df

if __name__ == "__main__":
    input_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\synthetic_data\gemini2.0FlashThinking"
    output_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\synthetic_data\gemini2.0FlashThinking"
    
    df = process_markdown_for_dataset(input_dir, output_dir)