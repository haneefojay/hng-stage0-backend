from fastapi import APIRouter, HTTPException, Request
import logging
from app.core.limiter import limiter
import httpx
from app.core.config import settings
from app.core.utils import get_current_utc_time
import html


router = APIRouter()
logger = logging.getLogger("hng-backend")

@router.get("/me")
@limiter.limit("10/minute")
async def get_my_profile(request: Request):
    logger.info(f"Incoming request: {request.method} {request.url} from {request.client.host if request.client else 'unknown'}")
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
    logger.info(f"Response for /me: {data}")
    return data