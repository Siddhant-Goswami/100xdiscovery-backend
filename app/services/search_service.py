import os
from groq import Groq
from typing import List
from app.models.user_profile import UserProfile

class SearchService:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        self.client = Groq(api_key=groq_api_key)

    async def search_profiles(self, query: str, profiles: List[UserProfile]) -> List[UserProfile]:
        if not profiles:
            return []
            
        # Convert profiles to a format suitable for few-shot learning
        profile_texts = [
            f"Profile {i}:\n"
            f"Name: {p.name}\n"
            f"Skills: {', '.join(p.skills)}\n"
            f"Bio: {p.bio}\n"
            f"Projects: {', '.join(p.projects)}\n"
            f"Interests: {', '.join(p.collaboration_interests)}"
            for i, p in enumerate(profiles)
        ]
        
        # Create the prompt for the LLM
        prompt = f"""You are a search assistant helping to find relevant user profiles based on a search query.

Search Query: "{query}"

Available Profiles:
{'\n\n'.join(profile_texts)}

Instructions:
1. Analyze each profile and determine if it matches the search query
2. Consider skills, bio, projects, and interests when matching
3. Return ONLY the profile numbers (0-based indices) that match, separated by commas
4. If no profiles match, return "none"
5. Format example: "0,2,3" or "none"

Matching Profile Numbers:"""

        # Get response from Groq
        response = self.client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1  # Lower temperature for more consistent results
        )
        
        # Parse response to get indices
        try:
            content = response.choices[0].message.content.strip().lower()
            if content == "none":
                return []
                
            indices = [int(idx.strip()) for idx in content.split(',')]
            return [profiles[i] for i in indices if i < len(profiles)]
        except (ValueError, IndexError):
            print(f"Error parsing LLM response: {response.choices[0].message.content}")
            return [] 