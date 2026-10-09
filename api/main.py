from __future__ import annotations

from api.routers import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Мопеды Новосибирск", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"], allow_headers=["*"], allow_credentials=False)
app.include_router(router)

