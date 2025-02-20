<div align="center">
  <img src="final-logo.png" alt="MK Distill Logo" width="200"/>
  <h1>Deepseek-R1-8B-MikroTik-Distilled</h1>
</div>

## Overview
This project aims to create a specialized, efficient LLM for MikroTik RouterOS by distilling knowledge from comprehensive data sources and state-of-the-art LLM models. The goal is to provide the most accurate MikroTik AI assistant with minimal compute requirements.

## Model & Dataset Access
- [direct link to Deepseek-R1-8B-MikroTik-Distilled-GGUF on huggingface](https://huggingface.co/vivek-dodia/Deepseek-R1-8B-MikroTik-Distilled-GGUF)
- [huggingface profile](https://huggingface.co/vivek-dodia)

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

