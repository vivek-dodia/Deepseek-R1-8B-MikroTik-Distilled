# MikroTik RouterOS Configuration Dataset

A structured dataset containing MikroTik RouterOS configuration guides and tutorials generated using Gemini 2.0 model_name="gemini-2.0-flash-exp".

## Dataset Details
- 3000+ configuration examples 
- Source: Synthetic data generated from DeepSeek LLM
- Format: Parquet file with structured columns

## Columns
- filename: Original MD file name
- title: Configuration guide title
- prompt: Scenario description
- implementation_steps: Step-by-step configuration instructions
- configuration_commands: Complete RouterOS commands
- parameter_explanations: Parameter details and usage
- verification_steps: Testing and validation steps
- security_practices: Security recommendations

## Generation
Created by processing raw markdown files into structured format using custom Python script. Each row represents one complete configuration guide with standardized sections.

## Usage
```python
import pandas as pd
df = pd.read_parquet('mikrotik_configs.parquet')