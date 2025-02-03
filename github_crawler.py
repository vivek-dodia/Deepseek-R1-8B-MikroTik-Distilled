import requests
import os
import time
import git
from datetime import datetime
from typing import List, Dict

class GitHubScraper:
    def __init__(self, token: str, base_path: str):
        self.headers = {'Authorization': f'token {token}'}
        self.base_path = base_path
        self.base_url = "https://api.github.com"
        
    def search_repos(self, query: str, sort: str = "stars", 
                    order: str = "desc", per_page: int = 100) -> List[Dict]:
        repos = []
        page = 1
        
        while len(repos) < 1000:
            url = f"{self.base_url}/search/repositories"
            params = {
                'q': query,
                'sort': sort,
                'order': order,
                'per_page': per_page,
                'page': page
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                break
                
            data = response.json()
            if not data['items']:
                break
                
            repos.extend(data['items'])
            page += 1
            time.sleep(2)  # Respect rate limits
            
        return repos[:1000]  # Ensure we return max 1000 repos

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
    # Replace with your GitHub token
    github_token = "ghp_TOKEN"
    base_path = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\github_repos"
    
    # Create directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    
    # Initialize scraper
    scraper = GitHubScraper(github_token, base_path)
    
    # Search query
    query = 'mikrotik in:name created:<2022-01-01'
    
    # Get repos
    print("Searching for repositories...")
    repos = scraper.search_repos(query)
    print(f"Found {len(repos)} repositories")
    
    # Clone repos
    successful_clones = 0
    for repo in repos:
        if scraper.clone_repo(repo['clone_url'], repo['name']):
            successful_clones += 1
            
    print(f"\nScript completed. Successfully cloned {successful_clones} repositories")

if __name__ == "__main__":
    main()