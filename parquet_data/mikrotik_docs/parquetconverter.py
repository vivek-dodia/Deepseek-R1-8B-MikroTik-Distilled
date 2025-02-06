import pandas as pd
import re
from pathlib import Path
from datetime import datetime

# Define input and output paths
input_dir = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\mikrotik_docs")
output_path = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\mikrotik_docs\documentation.parquet")

def clean_content(content):
    """Clean content while preserving code blocks and formatting."""
    # Remove trailing whitespace but preserve newlines
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    return '\n'.join(lines).strip()

def parse_sections(content):
    """Parse content into hierarchical sections."""
    sections = []
    lines = content.split('\n')
    current_section = {'title': '', 'content': [], 'level': 0}
    
    for line in lines:
        # Count leading '#' to determine heading level
        if line.startswith('#'):
            heading_level = len(re.match(r'^#+', line).group())
            heading_text = line.lstrip('#').strip()
            
            # If we have content in the current section, save it
            if current_section['title']:
                sections.append({
                    'title': current_section['title'],
                    'content': clean_content('\n'.join(current_section['content'])),
                    'level': current_section['level']
                })
            
            # Start new section
            current_section = {
                'title': heading_text,
                'content': [],
                'level': heading_level
            }
        elif current_section['title']:  # Add content to current section
            current_section['content'].append(line)
    
    # Add the last section
    if current_section['title'] and current_section['content']:
        sections.append({
            'title': current_section['title'],
            'content': clean_content('\n'.join(current_section['content'])),
            'level': current_section['level']
        })
    
    return sections

def parse_doc(content):
    """Parse a single documentation file into structured format."""
    try:
        # Extract document metadata
        doc_info = re.search(r'# Document Information\n(.*?)# Content', content, re.DOTALL)
        if doc_info:
            info_text = doc_info.group(1)
            title = re.search(r'Title: (.*?)\n', info_text).group(1)
            section = re.search(r'Section: (.*?)\n', info_text).group(1)
            source = re.search(r'Source: (.*?)[,\n]', info_text).group(1)
        else:
            raise ValueError("Could not find document information section")

        # Get main content
        main_content = re.search(r'# Content\n(.*)', content, re.DOTALL).group(1)
        
        # Parse sections
        sections = parse_sections(main_content)
        
        return {
            'doc_title': title,
            'doc_section': section,
            'source_url': source,
            'sections': sections
        }
    except Exception as e:
        print(f"Error parsing document: {e}")
        return None

def convert_docs_to_parquet(input_dir, output_path):
    """Convert all documentation files to a single Parquet file."""
    doc_rows = []
    processed_files = 0
    error_files = 0
    max_sections = 0

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Process files
    for md_file in input_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            doc_data = parse_doc(content)
            if doc_data:
                # Track maximum number of sections
                max_sections = max(max_sections, len(doc_data['sections']))
                
                # Create row dictionary
                row = {
                    'doc_title': doc_data['doc_title'],
                    'doc_section': doc_data['doc_section'],
                    'source_url': doc_data['source_url'],
                    'section_count': len(doc_data['sections'])
                }

                # Add section columns
                for i in range(max_sections):
                    if i < len(doc_data['sections']):
                        section = doc_data['sections'][i]
                        row[f'section_{i+1}_title'] = section['title']
                        row[f'section_{i+1}_content'] = section['content']
                        row[f'section_{i+1}_level'] = section['level']
                    else:
                        row[f'section_{i+1}_title'] = None
                        row[f'section_{i+1}_content'] = None
                        row[f'section_{i+1}_level'] = None

                doc_rows.append(row)
                processed_files += 1

                if processed_files % 100 == 0:
                    print(f"Processed {processed_files} files...")

        except Exception as e:
            print(f"Error processing file {md_file.name}: {e}")
            error_files += 1
            continue

    if not doc_rows:
        raise ValueError("No data was parsed successfully from any files")

    # Create DataFrame
    df = pd.DataFrame(doc_rows)

    # Save to Parquet
    df.to_parquet(output_path, index=False)

    print(f"\nProcessing complete:")
    print(f"Successfully processed: {processed_files} files")
    print(f"Files with errors: {error_files}")
    print(f"Number of documents: {len(df)}")
    print(f"Maximum sections in any document: {max_sections}")
    print(f"Average sections per document: {df['section_count'].mean():.1f}")
    print(f"Saved to {output_path}")

    # Show example of section hierarchy
    print("\nExample section hierarchy from first document:")
    first_doc = df.iloc[0]
    for i in range(int(first_doc['section_count'])):
        level = int(first_doc[f'section_{i+1}_level']) if pd.notna(first_doc[f'section_{i+1}_level']) else 1
        title = first_doc[f'section_{i+1}_title']
        print(f"{'  ' * (level-1)}{title}")


    return df

def main():
    try:
        print(f"Starting processing of documentation files from {input_dir}")
        df = convert_docs_to_parquet(input_dir, output_path)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()