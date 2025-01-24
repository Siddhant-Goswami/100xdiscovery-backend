from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import profiles, auth

app = FastAPI(title="100xEngineers Discovery Platform")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(profiles.router)

@app.get("/")
async def root():
    return {"message": "Welcome to 100xEngineers Discovery Platform API"} 