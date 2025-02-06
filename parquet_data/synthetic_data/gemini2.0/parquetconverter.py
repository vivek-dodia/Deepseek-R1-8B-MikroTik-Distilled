import os
import re
import pandas as pd
from tqdm import tqdm

class MDProcessor:
    def __init__(self, input_dir: str):
        self.input_dir = input_dir
        
    def clean_text(self, text: str) -> str:
        text = re.sub(r'```mikrotik\n', '', text)
        text = re.sub(r'```', '', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def extract_sections(self, content: str, filename: str) -> dict:
        # Extract title
        title_match = re.search(r'# (.*?)\n', content)
        title = title_match.group(1).strip() if title_match else ""
        
        # Extract Scenario Description as prompt
        scenario_match = re.search(r'## Scenario Description:\n(.*?)(?=\n## |$)', content, re.DOTALL)
        prompt = self.clean_text(scenario_match.group(1)) if scenario_match else ""
        
        # Extract other sections
        sections = {
            'filename': filename,
            'title': title,
            'prompt': prompt,
            'implementation_steps': '',
            'configuration_commands': '',
            'parameter_explanations': '',
            'verification_steps': '',
            'security_practices': '',
            'version_info': ''
        }
        
        section_patterns = {
            'implementation_steps': r'## Implementation Steps:\n(.*?)(?=\n## |$)',
            'configuration_commands': r'## Complete Configuration Commands:\n(.*?)(?=\n## |$)',
            'parameter_explanations': r'## Parameter Explanations:\n(.*?)(?=\n## |$)',
            'verification_steps': r'## Verification and Testing Steps:\n(.*?)(?=\n## |$)',
            'security_practices': r'## Security Best Practices:\n(.*?)(?=\n## |$)',
            'version_info': r'## Configuration for Specific RouterOS Versions:\n(.*?)(?=\n## |$)'
        }
        
        for key, pattern in section_patterns.items():
            match = re.search(pattern, content, re.DOTALL)
            sections[key] = self.clean_text(match.group(1)) if match else ""
            
        return sections

    def process_all_files(self) -> pd.DataFrame:
        data = []
        md_files = [f for f in os.listdir(self.input_dir) if f.endswith('.md')]
        
        for filename in tqdm(md_files, desc="Processing files"):
            filepath = os.path.join(self.input_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                sections = self.extract_sections(content, filename)
                data.append(sections)
            except Exception as e:
                print(f"\nError processing {filename}: {str(e)}")
                
        return pd.DataFrame(data)

    def save_parquet(self, output_path: str):
        print("Processing MD files...")
        df = self.process_all_files()
        
        print(f"\nProcessed {len(df)} files")
        print(f"Columns: {', '.join(df.columns)}")
        print("\nSample prompt:", df['prompt'].iloc[0][:100], "...")
        print("Saving to parquet...")
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_parquet(output_path, index=False)
        print(f"Saved to: {output_path}")

if __name__ == "__main__":
    input_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\synthetic_data\gemini2.0"
    output_path = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\synthetic_data\gemini2.0\mikrotik_configs.parquet"
    
    processor = MDProcessor(input_dir)
    processor.save_parquet(output_path)