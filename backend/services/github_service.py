import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {token}"} if token else {}

# Parse Repo URL into owner and repo name
def parse_repo_url(repo_url: str):
    parts = repo_url.rstrip("/").split("/")
    if len(parts) < 2:
        return None, None
    return parts[-2], parts[-1]

# Fetch Repo content
def fetch_repo_content(repo_url: str): 
    owner, repo = parse_repo_url(repo_url)
    if not owner or not repo:
        return {"Error": "Invalid repository URL"}
    
    # Get list of files from root directory
    repo_info = requests.get(f"https://api.github.com/repos/{owner}/{repo}", headers=headers).json()
    default_branch = repo_info.get("default_branch", "main")

    tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"
    tree_resp = requests.get(tree_url, headers=headers)

    if tree_resp.status_code != 200:
        return {"error": "Rate limit exceeded or Repo not found"}
    
    tree_data = tree_resp.json()
    file_data = ""
    file_count = 0
    max_files = 15  

   # Loop through every file in the repo
    for item in tree_data.get("tree", []):
        if file_count >= max_files:
            break

        path = item["path"]
        
        # Filter: Must be a 'blob' (file) and have the right extension
        if item["type"] == "blob" and path.endswith((".md", ".py", ".js", ".tsx", ".json", ".html", ".css")):
            
            # Skip lock files or huge configurations
            if "lock" in path or "config" in path:
                continue

            # Fetch content
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{default_branch}/{path}"
            file_resp = requests.get(raw_url, headers=headers)
            
            if file_resp.status_code == 200:
                content = file_resp.text
                file_data += f"\n\n--- FILE: {path} ---\n{content}"
                file_count += 1
                print(f"Fetched: {path}")

    if file_count == 0:
        return {"error": "No valid code files found"}

    return file_data