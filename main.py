from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET = "dev-secret-key"

class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/auth/login")
def login(data: LoginRequest):

    # ✅ test user
    if data.email == "admin@test.com" and data.password == "123456":
        token = jwt.encode(
            {
                "sub": data.email,
                "exp": datetime.utcnow() + timedelta(hours=8)
            },
            SECRET,
            algorithm="HS256"
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")