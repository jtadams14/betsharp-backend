# BetSharp Backend

This is the backend API for BetSharp — a horse racing picks app.

## Features
- User registration and login
- Free daily picks
- Premium picks (paid access)
- Simulated payment system
- JWT authentication
- Password encryption

## How to Run Locally
1. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Start the server:
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 10000
    ```

## Deploying to Render.com
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- Set environment variables (SECRET_KEY)

---
