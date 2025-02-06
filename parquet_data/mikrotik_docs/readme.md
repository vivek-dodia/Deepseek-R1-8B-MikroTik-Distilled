# MikroTik Technical Documentation Dataset

## Overview
A structured dataset containing MikroTik's technical documentation, prepared for LLM fine-tuning. The dataset preserves the hierarchical structure of the original documentation while maintaining technical accuracy and formatting.

## Dataset Statistics
- Total documents: 285
- Maximum sections per document: 91
- Average sections per document: 12.3
- Format: Parquet

## Data Structure
Each row represents a complete documentation page with the following fields:

### Metadata
- `doc_title`: Document title
- `doc_section`: Documentation category (e.g., RouterOS, Hardware)
- `source_url`: Original documentation URL
- `section_count`: Number of sections in document

### Content Fields (per section)
For each section (1 to n):
- `section_{n}_title`: Section heading
- `section_{n}_content`: Section content including code blocks
- `section_{n}_level`: Heading level (1 = main heading, 2 = subheading, etc.)

## Content Characteristics
- Preserved code blocks with syntax
- Maintained command examples and outputs
- Intact technical formatting
- Complete command parameters and descriptions
- Original markdown structure

## Typical Document Structure
1. Summary/Overview
2. Property/Parameter Descriptions
3. Configuration Examples
4. Troubleshooting/Notes

## Training Considerations
- Clean, consistently formatted technical content
- Hierarchical structure preserved through level indicators
- Complete context within each document
- Code blocks and command examples ready for model training
- Technical accuracy maintained in parameter descriptions

## Usage Example
```python
import pandas as pd

# Load the dataset
docs = pd.read_parquet('documentation.parquet')

# Access a document with all its sections
doc = docs.iloc[0]
print(f"Title: {doc['doc_title']}")

# Access specific sections
for i in range(int(doc['section_count'])):
    print(f"\nSection {i+1}: {doc[f'section_{i+1}_title']}")
    print(f"Content: {doc[f'section_{i+1}_content'][:200]}...")
```

## Data Quality
- Full preservation of technical content
- Consistent section numbering
- Maintained code formatting
- Preserved command syntax
- Complete parameter descriptions
- Original document hierarchy

## Source
Derived from official MikroTik documentation. Original formatting and technical accuracy preserved for training purposes.

## License
This dataset is derived from MikroTik's official documentation. Use should comply with MikroTik's terms of service and documentation licensing terms.