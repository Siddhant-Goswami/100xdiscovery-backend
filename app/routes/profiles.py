from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.user_profile import UserProfile, UserProfileCreate
from app.config.database import supabase
from app.services.search_service import SearchService
from uuid import UUID

router = APIRouter(prefix="/api")
search_service = SearchService()

@router.post("/profiles", response_model=UserProfile)
async def create_profile(profile: UserProfileCreate):
    try:
        response = supabase.table("profiles").insert(profile.model_dump()).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profiles", response_model=List[UserProfile])
async def list_profiles():
    try:
        response = supabase.table("profiles").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profiles/{profile_id}", response_model=UserProfile)
async def get_profile(profile_id: UUID):
    try:
        response = supabase.table("profiles").select("*").eq("id", str(profile_id)).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/search", response_model=List[UserProfile])
async def search_profiles(query: str):
    try:
        # Get all profiles
        response = supabase.table("profiles").select("*").execute()
        profiles = [UserProfile(**profile) for profile in response.data]
        
        # Perform search using Groq
        results = await search_service.search_profiles(query, profiles)
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 