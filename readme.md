# MikroTik Distilled LLM Project

## Overview
This project aims to create a specialized, efficient LLM for MikroTik RouterOS by distilling knowledge from comprehensive data sources and state-of-the-art LLM models. The goal is to provide the most accurate MikroTik AI assistant with minimal compute requirements.

## Model Access
- **Trained LLM Model**: [Deepseek-R1-8B-MikroTik-Distilled-GGUF](https://huggingface.co/vivek-dodia/Deepseek-R1-8B-MikroTik-Distilled-GGUF)
- **Project Author**: [vivek-dodia on HuggingFace](https://huggingface.co/vivek-dodia)

## Data Sources

### Official Documentation
- MikroTik master documentation PDF (PDF_Docs/) ✅
- MikroTik online documentation (Scraped_Data/mikrotik_docs/) ✅
- 1,750 pages of MikroTik documentation parsed into MD format ✅

### Community Resources
- Forum threads from MikroTik community (Scraped_Data/forum) ✅
- 700+ GitHub and GitLab repositories tagged with "MikroTik" (post RouterOS 7 + REST API release, Dec-2021)
  - Stored in Scraped_Data/github_repos/ & gitlab_repos/
  - Note: Repository data excluded from git due to size constraints ✅

### Synthetic Data Generation
Located in Scraped_Data/synthetic_data/

#### Models Used
1. Gemini 2.0 Flash Experience
   - Generated example tutorials for RouterOS core features
   - Dataset: [synthetic-data-gemini-2.0-ComplexConfiguration](https://huggingface.co/vivek-dodia/synthetic-data-gemini-2.0-ComplexConfiguration)
   - Dataset: [synthetic-data-gemini-2.0-ComplexTroubleshooting](https://huggingface.co/vivek-dodia/synthetic-data-gemini-2.0-ComplexTroubleshooting)

2. Deepseek Reasoner/R1
   - Created complex troubleshooting scenarios
   - Dataset: [synthetic-data-deepseekR1-ComplexTroubleshooting](https://huggingface.co/vivek-dodia/synthetic-data-deepseekR1-ComplexTroubleshooting)

3. Gemini 2.0 Flash Thinking Experience
   - Enhanced reasoning and problem-solving scenarios
   - Contributed to comprehensive troubleshooting dataset

## Repository Structure
This repository contains:
- Raw data files
- Dataset processing scripts
- Synthetic data generation code using various LLM APIs
- Data cleaning and preprocessing utilities

## Related Resources
- MikroTik OpenAPI Documentation: [mikrotik-openAPI](https://huggingface.co/vivek-dodia/mikrotik-openAPI)
- MikroTik Forum Threads: [mikrotik-threads](https://huggingface.co/vivek-dodia/mikrotik-threads)
- MikroTik Documentation: [mikrotik-docs](https://huggingface.co/vivek-dodia/mikrotik-docs)
- Repository Collections:
  - GitHub Repos: [mikrotik-github-repos](https://huggingface.co/vivek-dodia/mikrotik-github-repos)
  - GitLab Repos: [mikrotik-gitlab-repos](https://huggingface.co/vivek-dodia/mikrotik-gitlab-repos)

## Dataset Statistics
- MikroTik Documentation: 285 files
- GitHub Repositories: 62.6k files
- GitLab Repositories: 11.3k files
- Forum Threads: 1.53k entries
- OpenAPI Documentation: 6.63k entries
- Synthetic Data:
  - Complex Configuration: 3.03k examples
  - Complex Troubleshooting: 762 scenarios

Note: All datasets are available in cleaned parquet/jsonl formats on HuggingFace.