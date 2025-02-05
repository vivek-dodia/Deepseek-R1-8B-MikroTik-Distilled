# MikroTik Forum Discussions Dataset

## Overview
This dataset contains structured conversations from MikroTik forums, curated specifically for training Large Language Models (LLMs) on networking concepts, troubleshooting, and technical discussions. Each thread includes an initial question followed by community responses, preserving the natural flow of technical discussions.

## Dataset Structure
The data is stored in Parquet format with a wide-table structure where each row represents a complete thread:

- `thread_id`: Unique identifier for each discussion thread
- `thread_title`: Original title of the thread
- `section`: Forum section (e.g., RouterOS, Hardware)
- `question`: The initial question or problem statement
- `response_count`: Number of responses in the thread
- `response_1` to `response_n`: Sequential responses to the question

## Content
- Source: MikroTik Forum discussions
- Topics covered:
  - RouterOS configuration
  - Network troubleshooting
  - Hardware setup and compatibility
  - Performance optimization
  - Feature requests and discussions
  - Best practices and solutions

## Sample Usage
```python
import pandas as pd

# Load the dataset
df = pd.read_parquet('forum/threads.parquet')

# Access a complete thread
thread = df.iloc[0]
print(f"Question: {thread['question']}")
print(f"First response: {thread['response_1']}")
```

## Preprocessing
The dataset has been preprocessed to:
- Maintain markdown formatting for code blocks and technical content
- Preserve URLs and technical references
- Remove unnecessary separators and formatting artifacts
- Structure conversations in a format suitable for LLM training

## Dataset Statistics
- Each thread contains an initial question and variable number of responses
- Content includes technical discussions, configurations, and community knowledge
- Original formatting and links are preserved for technical accuracy

## Notes
- Content is focused on technical networking discussions
- Includes both questions and detailed community responses
- Suitable for training models on network engineering concepts and troubleshooting

## License
This dataset is derived from public forum discussions. Use should comply with MikroTik's terms of service and community guidelines.