from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import profile

app = FastAPI(title="HNG stage 0 Backend task")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router)