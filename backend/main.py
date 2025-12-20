from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

@app.get("/build_documentation")
def build_documentation():
    return {"status": "Server is running", "message": "Hello from FastAPI"}

@app.post("/test")
def test_endpoint(request: ReadMeRequest):
    print(f"Received URL: {request.repo_url}")
    print(f"Received Notes: {request.notes}")
    
    return {"message": "Data received", "url": request.repo_url, "notes": request.notes}