from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Point(BaseModel):
    id: int
    avito_id: str | None = None
    lat: float
    lon: float
    title: str | None = None
    price: int | None = None
    category: str | None = None
    url: str | None = None
    seller_name: str | None = None
    city: str | None = None


class SellerDetail(BaseModel):
    id: int
    avito_id: str | None = None
    name: str | None = None
    city: str | None = None
    url: str | None = None
    avatar: str | None = None
    rating: float | None = None
    reviews_count: int | None = None
    description: str | None = None
    locations: list[dict[str, Any]] = []
    services: list[dict[str, Any]] = []
    parts: list[dict[str, Any]] = []
    contacts: list[dict[str, Any]] = []
    ads: list[dict[str, Any]] = []

