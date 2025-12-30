# AI-Powered README Generator

This project is an AI-powered application designed to automate the creation of professional `README.md` files for GitHub repositories. It provides a simple web interface for users to submit a repository URL and optional notes, which are then processed by a FastAPI backend. The backend fetches code context from the specified repository and leverages the Google Gemini AI model to generate a comprehensive and well-structured `README.md` file.

The application aims to streamline the documentation process for developers, making it easier to generate high-quality project descriptions, features, installation guides, and usage instructions based on the actual codebase.

## Features

*   **Automated README Generation:** Generate professional `README.md` files from any public GitHub repository.
*   **AI-Powered Content:** Utilizes the Google Gemini API to intelligently analyze code context and generate relevant documentation.
*   **Customization with Notes:** Allows users to provide additional notes or specific instructions to guide the AI during README generation.
*   **GitHub Integration:** Fetches repository content and file structure directly from GitHub using the GitHub API.
*   **Multi-language Support:** Extracts code context from various file types, including Python (`.py`), JavaScript (`.js`), TypeScript (`.tsx`), Markdown (`.md`), JSON (`.json`), HTML (`.html`), and CSS (`.css`).
*   **User-Friendly Interface:** A simple and intuitive web frontend built with React for submitting repository details.
*   **Scalable Backend:** A FastAPI backend provides a robust and efficient API for handling requests.

## Technologies Used

The project is built using a modern tech stack, combining a React frontend with a Python FastAPI backend.

### Frontend

*   **React 19:** A JavaScript library for building user interfaces.
*   **Vite:** A fast build tool that provides a rapid development environment.
*   **TypeScript:** A superset of JavaScript that adds static typing.
*   **CSS:** For styling the user interface.

### Backend

*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.8+.
*   **Pydantic:** Used for data validation and settings management.
*   **Requests:** An elegant and simple HTTP library for Python.
*   **python-dotenv:** For managing environment variables.
*   **Google Generative AI (Gemini API):** The core AI model for generating README content.
*   **GitHub API:** For programmatically accessing repository content.

## Installation

To set up and run this project locally, you will need to install both the backend and frontend components.

### Prerequisites

*   **Python 3.8+:** For the FastAPI backend.
*   **Node.js & npm (or yarn):** For the React frontend.
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

### 3. Frontend Setup

Navigate to the `frontend` directory:

```bash
cd ../frontend
```

#### Install Node.js Dependencies

```bash
npm install
```

## Usage

Follow these steps to run the application and generate a README.

### 1. Start the Backend Server

From the `backend` directory (after activating your virtual environment):

```bash
uvicorn main:app --reload
```
The backend server will typically run on `http://localhost:8000`.

### 2. Start the Frontend Development Server

From the `frontend` directory:

```bash
npm run dev
```
The frontend application will typically open in your browser at `http://localhost:5173`.

### 3. Generate a README

1.  Open your web browser and navigate to the frontend application (e.g., `http://localhost:5173`).
2.  Enter the URL of a GitHub repository (e.g., `https://github.com/octocat/Spoon-Knife`) into the "Enter Repo URL" field.
3.  Optionally, add any specific notes or instructions in the "Additional Notes" textarea to guide the README generation.
4.  *(Note: The current frontend UI requires development to include a submit button and display mechanisms. Once implemented, submitting the form will trigger the backend process.)*
5.  After the backend processes the request, the generated `README.md` file will be saved in the `backend` directory as `generated_README.md`.

## Development Notes

*   **Frontend-Backend Communication:** The frontend will need to make a POST request to `http://localhost:8000/build_documentation` with the repository URL and notes.
*   **CORS Configuration:** The backend's `main.py` includes CORS settings configured to allow requests from `http://localhost:5174`. If your frontend runs on a different port (e.g., `http://localhost:5173` as is default for Vite), you might need to adjust the `origins` list in `backend/main.py` or configure your frontend to proxy API requests. For this README, it is assumed frontend calls `http://localhost:8000` from `http://localhost:5173`, and the backend `CORS` should be configured accordingly.

    ```python
    # backend/main.py
    origins = [
        "http://localhost:5173", # Update this to match your frontend's actual port
        "http://127.0.0.1:5173",
    ]
    ```

*   **Frontend UI Enhancement:** The `DataInput.tsx` component needs further development to handle input state changes, implement a submission button, display loading states, show errors, and render/download the generated README.

## Project Structure

```
.
├── backend/
│   ├── main.py                     # FastAPI application entry point
│   ├── services/
│   │   ├── github_service.py       # Handles fetching content from GitHub
│   │   └── llm_service.py          # Interacts with Google Gemini API for README generation
│   ├── .env.example                # Example for backend environment variables
│   └── generated_README.md         # Output file for generated READMEs
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.tsx                 # Main React component
│   │   ├── DataInput.tsx           # Component for user input (Repo URL, Notes)
│   │   ├── index.css
│   │   └── main.tsx                # Frontend entry point
│   ├── index.html                  # HTML template for the frontend
│   ├── package.json                # Frontend dependencies and scripts
│   ├── tsconfig.json               # TypeScript configuration
│   └── vite.config.ts              # Vite configuration
│
└── README.md                       # This file
```