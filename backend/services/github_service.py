import requests
import base64

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
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    response = requests.get(api_url)

    if response.status_code != 200:
        return {"error": "Could not fetch repo. Check URL."}
    
    items = response.json()
    file_data = ""

    for item in items:
        if item['type'] == 'file':
            if item['name'].endswith(('.md', '.txt', '.py', '.js', '.java', '.tsx', '.json')):

                file_response = requests.get(item['download_url'])

                if file_response.status_code == 200:
                    content = file_response.text
                    file_data += f"\n\n--- FILE: {item['name']} ---\n{content}"
    
    return file_data