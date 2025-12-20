from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.github_service import fetch_repo_content
from services.llm_service import generate_readme_text

app = FastAPI()

# React app runs on port 5174 
origins = [
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,    
    allow_credentials = True,   
    allow_methods = ["*"],     
    allow_headers = ["*"],     
)

class ReadMeRequest(BaseModel):
    repo_url: str
    notes: str = ""

@app.get("/heartbeat")
def read_heartbeat():
    return {"status": "Server is running", "message": "Hello from FastAPI"}

@app.post("/build_documentation")
def generate_readme(request: ReadMeRequest):
    print(f"Fetching repo: {request.repo_url}")

    code_context = fetch_repo_content(request.repo_url)

    if isinstance(code_context, dict) and "error" in code_context:
        return {"status": "error", "message": code_context["error"]}
    
    print(f"Fetched {len(code_context)} chars of code. Sending to Gemini...")

    readme_text = generate_readme_text(code_context, request.notes)

    output_file_path = "generated_README.md"
    with open(output_file_path, "w") as f:
        f.write(readme_text)

    print(f"Generated README.md saved to {output_file_path}")


    return {
        "status": "success",
        "readme": f"Generated README.md saved to {output_file_path}"
    }

@app.post("/test")
def test_endpoint(request: ReadMeRequest):
    print(f"Received URL: {request.repo_url}")
    print(f"Received Notes: {request.notes}")
    
    return {"message": "Data received", "url": request.repo_url, "notes": request.notes}