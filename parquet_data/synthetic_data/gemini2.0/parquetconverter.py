import os
import re
import pandas as pd
from tqdm import tqdm

class MDProcessor:
    def __init__(self, input_dir: str):
        self.input_dir = input_dir
        
    def clean_text(self, text: str) -> str:
        """Clean and format the input text by removing specific patterns.

        This function takes a string input and removes occurrences of specific
        code block markers and excessive whitespace. It is particularly useful
        for sanitizing text that may contain formatting artifacts from Markdown
        or similar markup languages.

        Args:
            text (str): The input string that needs to be cleaned.

        Returns:
            str: The cleaned and formatted version of the input text.
        """

        text = re.sub(r'```mikrotik\n', '', text)
        text = re.sub(r'```', '', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def extract_sections(self, content: str, filename: str) -> dict:
        """Extract sections from the given content string.

        This method processes the provided content to extract various sections,
        including the title, scenario description, and other predefined sections
        such as implementation steps, configuration commands, parameter
        explanations, verification steps, security practices, and version
        information. It uses regular expressions to locate and clean the
        relevant text segments. The extracted data is organized into a
        dictionary for easy access.

        Args:
            content (str): The content string from which sections are to be extracted.
            filename (str): The name of the file associated with the content.

        Returns:
            dict: A dictionary containing the extracted sections, with keys for each
                section and their
                corresponding cleaned text values.
        """

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
        """Process all Markdown files in the specified input directory.

        This function scans the input directory for files with a '.md'
        extension, reads their content, and extracts sections from each file.
        The extracted sections are collected into a list, which is then
        converted into a pandas DataFrame for further analysis or processing.
        The function also provides feedback on the processing status through a
        progress bar.

        Returns:
            pd.DataFrame: A DataFrame containing the extracted sections from all
            processed Markdown files.
        """

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
        """Save processed data to a Parquet file.

        This function processes Markdown files, generates a DataFrame from the
        processed data, and saves it to a specified Parquet file. It first
        prints the number of processed files and their columns, then it creates
        the necessary directories for the output path if they do not exist, and
        finally saves the DataFrame to the specified Parquet file.

        Args:
            output_path (str): The file path where the Parquet file will be saved.
        """

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