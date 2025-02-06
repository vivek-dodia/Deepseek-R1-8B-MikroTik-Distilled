import pandas as pd
import json
from pathlib import Path
import logging
from typing import List, Dict, Any
from tqdm import tqdm

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_dataframe_to_records(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Convert DataFrame to a list of consistent, flat dictionaries
    """
    records = []
    
    # Process each row
    for _, row in df.iterrows():
        # Create a flat dictionary with consistent types
        record = {
            'repo_name': str(row['repo_name']),
            'filename': str(row.get('filename', '')),
            'file_content': str(row.get('file_content', '')),
            'extension': str(row.get('extension', '')),
            'content_length': int(row.get('content_length', 0)),
            'line_count': int(row.get('line_count', 0)),
            'is_config': bool(row.get('is_config', False)),
            'is_source': bool(row.get('is_source', False)),
            'is_documentation': bool(row.get('is_documentation', False)),
            'has_networking': bool(row.get('has_networking', False)),
            'has_automation': bool(row.get('has_automation', False)),
            'config_type': str(row.get('config_type', 'unknown'))
        }
        
        records.append(record)
    
    return records

def create_huggingface_dataset(input_parquet: str, output_json: str):
    """
    Create a HuggingFace compatible dataset from parquet file
    """
    logger.info(f"Reading parquet file: {input_parquet}")
    df = pd.read_parquet(input_parquet)
    
    # Process the data
    logger.info("Processing records...")
    records = process_dataframe_to_records(df)
    
    # Create the final dataset structure
    dataset = {
        'data': records
    }
    
    # Ensure output directory exists
    output_path = Path(output_json)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save as JSONL instead of JSON for better compatibility
    logger.info(f"Saving dataset to: {output_json}")
    with open(output_json, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record) + '\n')
    
    # Print summary
    logger.info("\nDataset Creation Summary:")
    logger.info(f"Total records: {len(records)}")
    logger.info(f"Total repositories: {len(set(r['repo_name'] for r in records))}")
    
    # Print sample record for verification
    if records:
        logger.info("\nSample record structure:")
        logger.info(json.dumps(records[0], indent=2))
    
    return dataset

if __name__ == "__main__":
    input_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\gitlab_repos\gitlab_dataset.parquet"
    output_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\gitlab_repos\gitlab_repos.jsonl"  # Note: changed to .jsonl
    
    try:
        result = create_huggingface_dataset(input_file, output_file)
        
        # Print additional statistics
        unique_repos = set(r['repo_name'] for r in result['data'])
        print(f"\nRepository Statistics:")
        print(f"Total unique repositories: {len(unique_repos)}")
        print(f"Average files per repository: {len(result['data']) / len(unique_repos):.1f}")
        
        # Count file types
        config_files = sum(1 for r in result['data'] if r['is_config'])
        source_files = sum(1 for r in result['data'] if r['is_source'])
        doc_files = sum(1 for r in result['data'] if r['is_documentation'])
        
        print("\nFile Types Distribution:")
        print(f"Config files: {config_files}")
        print(f"Source files: {source_files}")
        print(f"Documentation files: {doc_files}")
        
    except Exception as e:
        logger.error(f"Error processing dataset: {str(e)}", exc_info=True)