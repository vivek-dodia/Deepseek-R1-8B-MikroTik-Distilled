

## **the idea is to gather all the mikrotik related information on internet + generate synthetic data from various state of the art LLM models and train a distilled mini LLM for the most accurate and least compute footprint mikrotik AI assistant.**

**data sources**

-   mikrotik master doc pdf - PDF_Docs/
-   mikrotik online documention - Scraped_Data/mikrotik_docs/
-   threads from mikrotik forum - Scraped_Data/forum
-   SYNTHETIC DATA generated from gemini 2.0 - Scraped_Data/synthetic_data/gemini2.0
-   SYNTHETIC DATA generated from deepseek R1 - Scraped_Data/synthetic_data/deepseek
-   700+ repos from github and gitlab which are tagged with "Mikrotik" which are created since Dec-2021 (release of Router OS 7 + rest api) are stored Scraped_Data/github_repos/ && gitlab_repos/ (cannot be pushed to git due to file size)