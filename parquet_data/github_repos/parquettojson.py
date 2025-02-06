import pandas as pd
import json
from pathlib import Path
import logging
from typing import List, Dict, Any
from tqdm import tqdm

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_dataframe_to_records(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Convert DataFrame to a list of consistent, flat dictionaries
    Handles all fields from the GitHub MikroTik dataset
    """
    records = []
    
    # Process each row with progress bar
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing records"):
        try:
            # Create a flat dictionary with consistent types
            record = {
                'repo_name': str(row['repo_name']),
                'filename': str(row.get('filename', '')),
                'file_content': str(row.get('file_content', '')),
                'extension': str(row.get('extension', '')),
                'content_length': int(row.get('content_length', 0)),
                'line_count': int(row.get('line_count', 0)),
                'commands_used': row.get('commands_used', '[]'),
                'config_type': str(row.get('config_type', 'unknown')),
                'code_patterns': row.get('code_patterns', '[]'),
                'has_networking': bool(row.get('has_networking', False)),
                'has_automation': bool(row.get('has_automation', False)),
                'has_security': bool(row.get('has_security', False)),
                'is_config': bool(row.get('is_config', False)),
                'is_source': bool(row.get('is_source', False)),
                'is_documentation': bool(row.get('is_documentation', False))
            }
            
            # Handle any non-serializable values
            for key, value in record.items():
                if not isinstance(value, (str, int, float, bool, list, dict, type(None))):
                    record[key] = str(value)
            
            records.append(record)
            
        except Exception as e:
            logger.warning(f"Error processing row: {str(e)}")
            continue
    
    return records

def create_huggingface_dataset(input_parquet: str, output_json: str):
    """
    Create a HuggingFace compatible dataset from parquet file
    """
    try:
        logger.info(f"Reading parquet file: {input_parquet}")
        df = pd.read_parquet(input_parquet)
        
        # Process the data
        logger.info("Converting records to JSONL format...")
        records = process_dataframe_to_records(df)
        
        if not records:
            logger.error("No records were processed successfully")
            return None
        
        # Ensure output directory exists
        output_path = Path(output_json)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save as JSONL
        logger.info(f"Saving dataset to: {output_json}")
        with open(output_json, 'w', encoding='utf-8') as f:
            for record in records:
                f.write(json.dumps(record) + '\n')
        
        # Create summary statistics
        dataset_stats = {
            'total_records': len(records),
            'total_repositories': len(set(r['repo_name'] for r in records)),
            'file_types': {
                'config_files': sum(1 for r in records if r['is_config']),
                'source_files': sum(1 for r in records if r['is_source']),
                'documentation_files': sum(1 for r in records if r['is_documentation'])
            },
            'features': {
                'networking': sum(1 for r in records if r['has_networking']),
                'automation': sum(1 for r in records if r['has_automation']),
                'security': sum(1 for r in records if r['has_security'])
            }
        }
        
        # Print summary
        logger.info("\nDataset Creation Summary:")
        logger.info(f"Total records: {dataset_stats['total_records']}")
        logger.info(f"Total repositories: {dataset_stats['total_repositories']}")
        
        logger.info("\nFile Types Distribution:")
        for file_type, count in dataset_stats['file_types'].items():
            logger.info(f"{file_type}: {count}")
        
        logger.info("\nFeatures Distribution:")
        for feature, count in dataset_stats['features'].items():
            logger.info(f"Files with {feature}: {count}")
        
        # Print sample record
        if records:
            logger.info("\nSample record structure:")
            logger.info(json.dumps(records[0], indent=2))
        
        return dataset_stats
        
    except Exception as e:
        logger.error(f"Error processing dataset: {str(e)}", exc_info=True)
        return None

def main():
    """Main execution function"""
    input_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\github_repos\github_dataset.parquet"
    output_file = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\github_repos\github_repos.jsonl"
    
    try:
        # Process the dataset
        stats = create_huggingface_dataset(input_file, output_file)
        
        if stats:
            # Calculate and print additional statistics
            avg_files_per_repo = stats['total_records'] / stats['total_repositories']
            logger.info(f"\nRepository Statistics:")
            logger.info(f"Average files per repository: {avg_files_per_repo:.1f}")
            
            # Save statistics to a JSON file
            stats_file = Path(output_file).with_suffix('.stats.json')
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2)
            logger.info(f"\nStatistics saved to: {stats_file}")
            
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()