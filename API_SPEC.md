# 100xEngineers Discovery Platform API Specification

Base URL: `https://soviet-tiff-100xengineers-e7398f49.koyeb.app`

## Authentication
The API uses JWT-based authentication. Users must sign up and sign in to obtain an access token.

### Authentication Endpoints

#### 1. Sign Up
Create a new user account.

**Endpoint:** `POST /auth/signup`

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "strongpassword123"
}
```

**Success Response (When Email Verification Disabled) (200 OK):**
```json
{
    "message": "Signup successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer",
    "user": {
        "id": "uuid",
        "email": "user@example.com",
        "aud": "authenticated",
        "role": "authenticated",
        "email_confirmed_at": "2024-01-24T10:00:00Z",
        "last_sign_in_at": "2024-01-24T10:00:00Z",
        "created_at": "2024-01-24T10:00:00Z",
        "updated_at": "2024-01-24T10:00:00Z"
    }
}
```

**Success Response (When Email Verification Enabled) (200 OK):**
```json
{
    "message": "Signup successful. Please check your email for verification.",
    "user": {
        "id": "uuid",
        "email": "user@example.com",
        "aud": "authenticated",
        "role": "authenticated",
        "created_at": "2024-01-24T10:00:00Z",
        "updated_at": "2024-01-24T10:00:00Z"
    }
}
```

**Error Response (400 Bad Request):**
```json
{
    "detail": "User already registered"
}
```

#### 2. Sign In
Sign in with email and password to obtain an access token.

**Endpoint:** `POST /auth/signin`

**Request Body:**
```json
{
    "email": "user@example.com",
    "password": "strongpassword123"
}
```

**Success Response (200 OK):**
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer",
    "user": {
        "id": "uuid",
        "email": "user@example.com",
        "aud": "authenticated",
        "role": "authenticated",
        "email_confirmed_at": "2024-01-24T10:00:00Z",
        "last_sign_in_at": "2024-01-24T10:00:00Z",
        "created_at": "2024-01-24T10:00:00Z",
        "updated_at": "2024-01-24T10:00:00Z"
    }
}
```

**Error Response (401 Unauthorized):**
```json
{
    "detail": "Incorrect email or password"
}
```

## Protected API Endpoints
All the following endpoints require authentication. Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

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
    "portfolio_url": "https://johndoe.dev",
    "user_id": "uuid"
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
        "portfolio_url": "string",
        "user_id": "uuid"
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
    "portfolio_url": "string",
    "user_id": "uuid"
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
        "portfolio_url": "string",
        "user_id": "uuid"
    }
]
```

## Error Handling

All endpoints may return the following error responses:

**401 Unauthorized:**
```json
{
    "detail": "Could not validate credentials"
}
```

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

1. **Authentication:**
   - Store the access token securely (e.g., in HttpOnly cookies)
   - Include the token in all API requests
   - Handle token expiration and refresh flows
   - Implement proper logout by removing the token

2. **Error Handling:**
   - Handle authentication errors (401) by redirecting to login
   - Display appropriate error messages to users
   - Implement retry logic for failed requests

3. **Search Implementation:**
   - The search endpoint accepts natural language queries
   - Results are ranked by relevance
   - Empty array is returned if no matches are found

4. **Profile IDs:**
   - Store profile IDs for referencing specific profiles
   - Use UUIDs for profile identification

5. **Optional Fields:**
   - `portfolio_url` is optional and may be null
   - Handle null values appropriately in the UI

6. **Arrays:**
   - `skills`, `projects`, and `collaboration_interests` are always arrays
   - They may be empty but will never be null 