# 100xEngineers Discovery Platform Backend

A FastAPI backend for the 100xEngineers Discovery Platform, featuring user profiles and LLM-powered search functionality.

## Features

- User profile management (CRUD operations)
- Natural language search using Groq LLM
- Supabase integration for data storage

## Prerequisites

- Python 3.8+
- Supabase account
- Groq API key

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/100xdiscovery-backend.git
cd 100xdiscovery-backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` with your actual credentials.

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /api/profiles` - Create a new user profile
- `GET /api/profiles` - List all profiles
- `GET /api/profiles/{id}` - Get a specific profile
- `POST /api/search` - Search profiles using natural language

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 