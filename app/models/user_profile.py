from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class UserProfileCreate(BaseModel):
    name: str
    bio: str
    skills: List[str]
    projects: List[str]
    collaboration_interests: List[str]
    portfolio_url: Optional[str] = None

class UserProfile(UserProfileCreate):
    id: UUID
    
    class Config:
        from_attributes = True 