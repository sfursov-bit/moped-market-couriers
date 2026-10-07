from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import router

app = FastAPI(
    title="Биржа мопедов — карта",
    description="Карта компаний (Авито): аренда, продажа, ремонт, выкуп, запчасти. Новосибирск.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(router)
