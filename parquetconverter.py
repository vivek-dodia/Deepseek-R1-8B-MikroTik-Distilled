import pandas as pd
from pathlib import Path

INPUT_DIR = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\cleaned_data\forum")
OUTPUT_DIR = Path(r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\forum")

def convert_to_parquet():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = []
    
    for file in INPUT_DIR.glob("*.md"):
        with open(file, 'r', encoding='utf-8') as f:
            data.append({
                'filename': file.name,
                'content': f.read(),
                'size': file.stat().st_size,
                'modified_date': file.stat().st_mtime
            })
    
    df = pd.DataFrame(data)
    output_file = OUTPUT_DIR / "forum_dataset.parquet"
    df.to_parquet(output_file, compression='snappy')
    print(f"Converted {len(data)} files to Parquet format")

if __name__ == "__main__":
    convert_to_parquet()