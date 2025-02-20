import requests
import os
import time
import git
from datetime import datetime
from typing import List, Dict

class GitLabScraper:
    def __init__(self, token: str, base_path: str):
        self.headers = {'PRIVATE-TOKEN': token}
        self.base_path = base_path
        self.base_url = "https://gitlab.com/api/v4"
        
    def search_repos(self, search: str, created_before: str) -> List[Dict]:
        repos = []
        page = 1
        
        while True:
            url = f"{self.base_url}/search"
            params = {
                'scope': 'projects',
                'search': search,
                'created_before': created_before,
                'order_by': 'stars',
                'sort': 'desc',
                'per_page': 100,
                'page': page
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                break
                
            data = response.json()
            if not data:
                break
                
            repos.extend(data)
            page += 1
            time.sleep(1)  # Respect rate limits
            
            if len(repos) >= 1000:
                break
                
        return repos[:1000]

    def clone_repo(self, repo_url: str, repo_name: str) -> bool:
        target_path = os.path.join(self.base_path, repo_name)
        
        if os.path.exists(target_path):
            print(f"Skipping {repo_name}: Already exists")
            return False
            
        try:
            git.Repo.clone_from(repo_url, target_path)
            print(f"Successfully cloned: {repo_name}")
            return True
        except Exception as e:
            print(f"Failed to clone {repo_name}: {str(e)}")
            return False

def main():
    # Replace with your GitLab token
    gitlab_token = "glpat-TOKEN"
    base_path = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\gitlab_repos"
    
    # Create directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    
    # Initialize scraper
    scraper = GitLabScraper(gitlab_token, base_path)
    
    # Search params
    search_term = "mikrotik"
    created_before = "2022-01-01T00:00:00Z"
    
    # Get repos
    print("Searching for repositories...")
    repos = scraper.search_repos(search_term, created_before)
    print(f"Found {len(repos)} repositories")
    
    # Clone repos
    successful_clones = 0
    for repo in repos:
        if scraper.clone_repo(repo['http_url_to_repo'], repo['path']):
            successful_clones += 1
            
    print(f"\nScript completed. Successfully cloned {successful_clones} repositories")

if __name__ == "__main__":
    main()