# 100xEngineers Discovery Platform API Specification

Base URL: `https://soviet-tiff-100xengineers-e7398f49.koyeb.app`

## Authentication
Currently, the API is open and doesn't require authentication.

## API Endpoints

### 1. Create User Profile
Create a new user profile in the platform.

**Endpoint:** `POST /api/profiles`

**Request Body:**
```json
{
    "name": "string",
    "bio": "string",
    "skills": ["string"],
    "projects": ["string"],
    "collaboration_interests": ["string"],
    "portfolio_url": "string" // optional
}
```

**Example Request:**
```json
{
    "name": "John Doe",
    "bio": "Full Stack Developer with 5 years of experience",
    "skills": ["Python", "React", "FastAPI", "AWS"],
    "projects": ["E-commerce Platform", "AI Chatbot"],
    "collaboration_interests": ["Open Source", "AI/ML Projects"],
    "portfolio_url": "https://johndoe.dev"
}
```

**Success Response (200 OK):**
```json
{
    "id": "uuid",
    "name": "John Doe",
    "bio": "Full Stack Developer with 5 years of experience",
    "skills": ["Python", "React", "FastAPI", "AWS"],
    "projects": ["E-commerce Platform", "AI Chatbot"],
    "collaboration_interests": ["Open Source", "AI/ML Projects"],
    "portfolio_url": "https://johndoe.dev"
}
```

### 2. List All Profiles
Retrieve all user profiles.

**Endpoint:** `GET /api/profiles`

**Success Response (200 OK):**
```json
[
    {
        "id": "uuid",
        "name": "string",
        "bio": "string",
        "skills": ["string"],
        "projects": ["string"],
        "collaboration_interests": ["string"],
        "portfolio_url": "string"
    }
]
```

### 3. Get Specific Profile
Retrieve a specific user profile by ID.

**Endpoint:** `GET /api/profiles/{profile_id}`

**Parameters:**
- `profile_id`: UUID of the profile

**Success Response (200 OK):**
```json
{
    "id": "uuid",
    "name": "string",
    "bio": "string",
    "skills": ["string"],
    "projects": ["string"],
    "collaboration_interests": ["string"],
    "portfolio_url": "string"
}
```

**Error Response (404 Not Found):**
```json
{
    "detail": "Profile not found"
}
```

### 4. Search Profiles
Search for profiles using natural language queries.

**Endpoint:** `POST /api/search`

**Query Parameters:**
- `query`: string - Natural language search query

**Example Queries:**
- `python developer interested in AI`
- `frontend developer with React experience`
- `looking for open source collaborators`

**Success Response (200 OK):**
```json
[
    {
        "id": "uuid",
        "name": "string",
        "bio": "string",
        "skills": ["string"],
        "projects": ["string"],
        "collaboration_interests": ["string"],
        "portfolio_url": "string"
    }
]
```

## Error Handling

All endpoints may return the following error responses:

**400 Bad Request:**
```json
{
    "detail": "Error message explaining what went wrong"
}
```

**500 Internal Server Error:**
```json
{
    "detail": "Internal server error"
}
```

## Response Headers

All responses include the following headers:
- `Content-Type: application/json`

## Rate Limiting
Currently, there are no rate limits implemented.

## Notes for Frontend Developers

1. **Error Handling:**
   - Always handle both successful and error responses
   - Display appropriate error messages to users

2. **Search Implementation:**
   - The search endpoint accepts natural language queries
   - Results are ranked by relevance
   - Empty array is returned if no matches are found

3. **Profile IDs:**
   - Store profile IDs for referencing specific profiles
   - Use UUIDs for profile identification

4. **Optional Fields:**
   - `portfolio_url` is optional and may be null
   - Handle null values appropriately in the UI

5. **Arrays:**
   - `skills`, `projects`, and `collaboration_interests` are always arrays
   - They may be empty but will never be null 