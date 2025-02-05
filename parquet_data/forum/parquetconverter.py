import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# Define input and output paths
input_dir = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\forum")
output_path = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\forum\threads.parquet")

def clean_content(text):
    """Clean the content while preserving markdown formatting."""
    # Remove trailing separator if it exists
    text = re.sub(r'\s*---\s*$', '', text)
    # Remove extra whitespace but preserve markdown formatting
    text = '\n'.join(line.rstrip() for line in text.splitlines())
    return text.strip()

def parse_thread(content):
    """Parse a single thread into a dictionary with question and responses."""
    try:
        # Extract metadata
        thread_id = re.search(r'Thread ID: (\d+)', content).group(1)
        title = re.search(r'Title: (.*?)\n', content).group(1)
        section = re.search(r'Section: (.*?)\n', content).group(1)
        
        # Initialize thread data
        thread_data = {
            'thread_id': thread_id,
            'thread_title': title,
            'section': section,
            'question': None,
            'responses': [],
            'response_count': 0
        }
        
        # Parse content into sections
        current_section = ""
        current_type = None
        
        for line in content.split('\n'):
            if line.startswith('## Initial Question'):
                if current_type == 'response' and current_section:
                    thread_data['responses'].append(clean_content(current_section))
                current_type = 'question'
                current_section = ""
            elif line.startswith('## Response'):
                if current_type == 'question' and current_section:
                    thread_data['question'] = clean_content(current_section)
                elif current_type == 'response' and current_section:
                    thread_data['responses'].append(clean_content(current_section))
                current_type = 'response'
                current_section = ""
            elif current_type:
                current_section += line + "\n"
        
        # Add the last section
        if current_type == 'question' and current_section:
            thread_data['question'] = clean_content(current_section)
        elif current_type == 'response' and current_section:
            thread_data['responses'].append(clean_content(current_section))
        
        thread_data['response_count'] = len(thread_data['responses'])
        return thread_data
    except Exception as e:
        print(f"Error parsing thread: {e}")
        return None

def convert_threads_to_parquet(input_dir, output_path):
    """Convert all thread files to a single wide-format Parquet file."""
    thread_rows = []
    processed_files = 0
    error_files = 0
    max_responses = 0
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Process files and build dataset
    for md_file in input_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            thread_data = parse_thread(content)
            if thread_data:
                # Update max responses count
                max_responses = max(max_responses, len(thread_data['responses']))
                
                # Create row dictionary
                row = {
                    'thread_id': thread_data['thread_id'],
                    'thread_title': thread_data['thread_title'],
                    'section': thread_data['section'],
                    'question': thread_data['question'],
                    'response_count': thread_data['response_count']
                }
                
                # Add response columns
                for i in range(max_responses):
                    response_num = i + 1
                    response_content = (thread_data['responses'][i] 
                                     if i < len(thread_data['responses']) 
                                     else None)
                    row[f'response_{response_num}'] = response_content
                
                thread_rows.append(row)
                processed_files += 1
                
                if processed_files % 100 == 0:
                    print(f"Processed {processed_files} files...")
                    
        except Exception as e:
            print(f"Error processing file {md_file.name}: {e}")
            error_files += 1
            continue
    
    if not thread_rows:
        raise ValueError("No data was parsed successfully from any files")
    
    # Create DataFrame
    df = pd.DataFrame(thread_rows)
    
    # Save to Parquet
    df.to_parquet(output_path, index=False)
    
    print(f"\nProcessing complete:")
    print(f"Successfully processed: {processed_files} files")
    print(f"Files with errors: {error_files}")
    print(f"Number of threads: {len(df)}")
    print(f"Maximum responses in any thread: {max_responses}")
    print(f"Average responses per thread: {df['response_count'].mean():.1f}")
    print(f"Saved to {output_path}")
    
    # Show example
    print("\nExample thread structure (truncated):")
    example_columns = ['thread_id', 'thread_title', 'question']
    example_columns.extend([f'response_{i+1}' for i in range(min(3, max_responses))])
    print("\nFirst thread (first 3 responses):")
    print(df[example_columns].head(1))
    
    return df

def main():
    try:
        print(f"Starting processing of .md files from {input_dir}")
        df = convert_threads_to_parquet(input_dir, output_path)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()