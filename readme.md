# MikroTik Distilled LLM Project

## Overview
This project aims to create a specialized, efficient LLM for MikroTik RouterOS by distilling knowledge from comprehensive data sources and state-of-the-art LLM models. The goal is to provide the most accurate MikroTik AI assistant with minimal compute requirements.

## Model Access
- **Trained LLM Model**: [Deepseek-R1-8B-MikroTik-Distilled-GGUF](https://huggingface.co/vivek-dodia/Deepseek-R1-8B-MikroTik-Distilled-GGUF)
- **Project Author**: [vivek-dodia on HuggingFace](https://huggingface.co/vivek-dodia)

## Data Sources

### Community data

- MikroTik online documentation
- 1,750 pages of MikroTik documentation parsed into MD format
- Forum threads from MikroTik community
- 700+ GitHub and GitLab repositories tagged with "MikroTik" (post RouterOS 7 + REST API release, Dec-2021)

### Synthetic Data Generation

#### Models Used
1. Gemini 2.0 Flash Experience
2. Deepseek Reasoner/R1
3. Gemini 2.0 Flash Thinking Experience


## Repository Structure
This repository contains:
- Raw data files
- Dataset processing scripts
- Synthetic data generation code using various LLM APIs
- Data cleaning and preprocessing utilities


## Dataset Statistics
- MikroTik Documentation: 285 files - https://huggingface.co/datasets/vivek-dodia/mikrotik-docs
- GitHub Repositories: 62.6k files - https://huggingface.co/datasets/vivek-dodia/mikrotik-github-repos
- GitLab Repositories: 11.3k files - https://huggingface.co/datasets/vivek-dodia/mikrotik-gitlab-repos
- Forum Threads: 1.53k entries - https://huggingface.co/datasets/vivek-dodia/mikrotik-threads
- Mikrotik OpenAPI Documentation: 6.63k entries - https://huggingface.co/datasets/vivek-dodia/mikrotik-openAPI
- Synthetic Data:
  - Gemini 2.0 Flash Thinking Experience-Complex Configuration: 3.03k examples - https://huggingface.co/datasets/vivek-dodia/synthetic-data-gemini-2.0-ComplexConfigurations
  - Gemini 2.0 Flash Experience-Complex Troubleshooting: 762 scenarios - https://huggingface.co/datasets/vivek-dodia/synthetic-data-gemini-2.0-ComplexTroubleshooting
  - Deepseek R1-Complex Troubleshooting: 87 scenarios - https://huggingface.co/datasets/vivek-dodia/synthetic-data-deepseekR1-ComplexTroubleshooting
Note: All datasets are available in cleaned parquet/jsonl formats on HuggingFace.

