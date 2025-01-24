from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from app.config.database import supabase

router = APIRouter(tags=["authentication"])

class UserAuth(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup")
async def signup(user_data: UserAuth):
    try:
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password
        })
        
        # If email confirmation is disabled, user can login immediately
        if response.user and response.session:
            return {
                "message": "Signup successful",
                "access_token": response.session.access_token,
                "token_type": "bearer",
                "user": response.user
            }
        
        # If email confirmation is enabled
        return {
            "message": "Signup successful. Please check your email for verification.",
            "user": response.user
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/signin")
async def signin(user_data: UserAuth):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        
        if not response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
            
        return {
            "access_token": response.session.access_token,
            "token_type": "bearer",
            "user": response.user
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        ) 