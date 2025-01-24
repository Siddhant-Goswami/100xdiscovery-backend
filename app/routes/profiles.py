from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.user_profile import UserProfile, UserProfileCreate
from app.config.database import supabase
from app.services.search_service import SearchService
from app.auth.auth import get_current_user
from uuid import UUID

router = APIRouter(tags=["profiles"])
search_service = SearchService()

@router.post("/profiles", response_model=UserProfile)
async def create_profile(profile: UserProfileCreate, current_user: dict = Depends(get_current_user)):
    try:
        # Use the authenticated user's ID as the profile ID
        profile_data = profile.model_dump()
        profile_data["id"] = current_user.id
        
        response = supabase.table("profiles").insert(profile_data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profiles", response_model=List[UserProfile])
async def list_profiles(current_user: dict = Depends(get_current_user)):
    try:
        response = supabase.table("profiles").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profiles/{profile_id}", response_model=UserProfile)
async def get_profile(profile_id: UUID, current_user: dict = Depends(get_current_user)):
    try:
        response = supabase.table("profiles").select("*").eq("id", str(profile_id)).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/search", response_model=List[UserProfile])
async def search_profiles(query: str, current_user: dict = Depends(get_current_user)):
    try:
        # Get all profiles
        response = supabase.table("profiles").select("*").execute()
        profiles = [UserProfile(**profile) for profile in response.data]
        
        # Perform search using Groq
        results = await search_service.search_profiles(query, profiles)
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 