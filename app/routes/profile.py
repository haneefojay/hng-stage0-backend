from fastapi import APIRouter, HTTPException, Request
from app.core.limiter import limiter
import httpx
from app.core.config import settings
from app.core.utils import get_current_utc_time
import html


router = APIRouter()

@router.get("/me")
@limiter.limit("10/minute")
async def get_my_profile(request: Request):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            cat_fact = html.unescape(response.json().get("fact", "No fact available."))
    except Exception as e:
        cat_fact = "Could not fetch cat fact at the moment."
    
    data = {
        "status": "success",
        "user": {
            "email": settings.EMAIL,
            "name": settings.FULL_NAME,
            "stack": settings.STACK
        },
        "timestamp": get_current_utc_time(),
        "fact": cat_fact
    }
    return data