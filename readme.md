<div align="center">
  <img src="final-logo.png" alt="MK Distill Logo" width="250"/>
  <h1>Deepseek-R1-8B-MikroTik-Distilled</h1>
</div>

## Overview
A specialized, efficient LLM for MikroTik RouterOS based on deepseek-r1 8b has been developed by distilling knowledge from comprehensive data sources and state-of-the-art LLM models. The end result is an accurate MikroTik LLM assistant that operates with minimal compute requirements. This project emerged from my interest in cool shit and the simple joy of building something unique - where networking meets machine learning/AI in an exciting combination as a passion project.
## Model & Dataset Access

- [huggingface profile](https://huggingface.co/vivek-dodia)
- [direct link to Deepseek-R1-8B-MikroTik-Distilled-GGUF on huggingface](https://huggingface.co/vivek-dodia/Deepseek-R1-8B-MikroTik-Distilled-GGUF)

## Data Sources

### Community data

- MikroTik online documentation
- 1,750 pages of MikroTik documentation parsed into MD format
- Forum threads from MikroTik community
- 700+ GitHub and GitLab repositories tagged with "MikroTik" (post RouterOS 7 + REST API release, Dec-2021)

### Synthetic Data Generation

#### Models Used
- Gemini 2.0 Flash Experience via api
- Deepseek Reasoner/R1 via api
- Gemini 2.0 Flash Thinking Experience via api


## Repository Structure
This repository contains:
- Raw data files
- Dataset processing scripts
- Synthetic data generation code using various LLM APIs
- Data cleaning and preprocessing utilities

- **Scraped_Data/** - Raw scraped data in MD format
- **cleaned_data/** - Cleaned and processed data from raw MD format
- **cleaners/** - Python scripts for data cleaning
- **crawlers/** - Web scraping code using crawl4ai
- **gitingest/** - GitHub/GitLab repository processing utilities
- **logs/** - Execution logs from all Python scripts
- **openapi/** - RouterOS 7 YAML OpenAPI specification
- **parquet_data/** - Final parquet datasets uploaded to HuggingFace
- **requirements.txt** - Python package dependencies for running the scripts

Note: All datasets are available in cleaned parquet/jsonl formats on HuggingFace.

