# AI-Powered README Generator Backend

This project is an AI-powered backend application designed to automate the creation of professional `README.md` files for GitHub repositories. It provides a FastAPI endpoint that receives a repository URL and optional notes as an HTTP request. The backend then fetches code context from the specified repository and leverages the Google Gemini AI model to generate a comprehensive and well-structured `README.md` file.

The application aims to streamline the documentation process for developers by intelligently analyzing codebase content and generating high-quality project descriptions, features, installation guides, and usage instructions.

## Features

*   **Automated README Generation:** Generate professional `README.md` files from any public GitHub repository.
*   **AI-Powered Content:** Utilizes the Google Gemini API to intelligently analyze code context and generate relevant documentation.
*   **Customization with Notes:** Allows users to provide additional notes or specific instructions to guide the AI during README generation.
*   **GitHub Integration:** Fetches repository content and file structure directly from GitHub using the GitHub API.
*   **Multi-language Code Context:** Extracts code context from various file types, including Python (`.py`), JavaScript (`.js`), TypeScript (`.tsx`), Markdown (`.md`), JSON (`.json`), HTML (`.html`), and CSS (`.css`).
*   **Robust FastAPI Backend:** Provides an efficient and scalable API for handling requests.

## Technologies Used

The project is a backend application built with Python FastAPI.

### Backend

*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.8+.
*   **Pydantic:** Used for data validation and settings management.
*   **Requests:** An elegant and simple HTTP library for Python.
*   **python-dotenv:** For managing environment variables.
*   **Google Generative AI (Gemini API):** The core AI model for generating README content.
*   **GitHub API:** For programmatically accessing repository content.

## Installation

To set up and run this project locally, you will need to install the backend components.

### Prerequisites

*   **Python 3.8+:** For the FastAPI backend.
*   **Git:** To clone the repository.

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/your-username/ai-readme-generator.git
cd ai-readme-generator
```

### 2. Backend Setup

Navigate to the `backend` directory and set up the Python environment.

```bash
cd backend
```

#### Install Python Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
pip install fastapi uvicorn pydantic requests python-dotenv google-generativeai
```

#### Environment Variables

Create a `.env` file in the `backend` directory with the following content:

```env
GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

*   **`GITHUB_TOKEN`**: Generate a Personal Access Token from your GitHub settings (Settings -> Developer settings -> Personal access tokens -> Tokens (classic)). Ensure it has at least `repo` scope to access private repositories or `public_repo` scope for public ones.
*   **`GEMINI_API_KEY`**: Obtain an API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage

Follow these steps to run the backend application and generate a README.

### 1. Start the Backend Server

From the `backend` directory (after activating your virtual environment):

```bash
uvicorn main:app --reload
```
The backend server will typically run on `http://localhost:8000`.

### 2. Generate a README via API Request

Once the backend server is running, you can send an HTTP POST request to the `/build_documentation` endpoint.

**Endpoint:** `POST http://localhost:8000/build_documentation`

**Request Body (JSON):**

```json
{
  "repo_url": "https://github.com/octocat/Spoon-Knife",
  "notes": "This is a simple demo project. Please highlight the main purpose and technologies used."
}
```

You can use a tool like `curl`, Postman, Insomnia, or any HTTP client to make this request.

**Example using `curl`:**

```bash
curl -X POST "http://localhost:8000/build_documentation" \
     -H "Content-Type: application/json" \
     -d '{
           "repo_url": "https://github.com/octocat/Spoon-Knife",
           "notes": "This is a simple demo project. Please highlight the main purpose and technologies used."
         }'
```

Upon successful processing, the generated `README.md` content will be saved as `generated_README.md` in the `backend` directory. The API response will also confirm the save location.

## Development Notes

*   **CORS Configuration:** The `backend/main.py` file includes CORS settings configured to allow requests from `http://localhost:5174`. If you intend to connect a client application from a different origin, you may need to adjust the `origins` list in `backend/main.py`.

## Project Structure

```
.
├── backend/
│   ├── main.py                     # FastAPI application entry point
│   ├── services/
│   │   ├── github_service.py       # Handles fetching content from GitHub
│   │   └── llm_service.py          # Interacts with Google Gemini API for README generation
│   ├── .env.example                # Example for backend environment variables
│   ├── generated_README.md         # Output file for generated READMEs
│   └── venv/                       # Python virtual environment (if created)
│
└── README.md                       # This file
```