from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import profiles, auth

app = FastAPI(
    title="100xEngineers Discovery Platform",
    description="API for the 100xEngineers Discovery Platform",
    version="1.0.0"
)

# Configure CORS with more specific settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "https://soviet-tiff-100xengineers-e7398f49.koyeb.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Mount the routers with explicit prefixes
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(profiles.router, prefix="/api", tags=["profiles"])

@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Welcome to 100xEngineers Discovery Platform API",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json"
    } 