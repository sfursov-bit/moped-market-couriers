from __future__ import annotations

from datetime import datetime
from typing import Any

from sqlalchemy import JSON, Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Seller(Base):
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    avito_id: Mapped[str | None] = mapped_column(String(64), unique=True, index=True)
    name: Mapped[str | None] = mapped_column(String(255))
    city: Mapped[str | None] = mapped_column(String(128), index=True)
    url: Mapped[str | None] = mapped_column(Text)
    avatar: Mapped[str | None] = mapped_column(Text)
    rating: Mapped[float | None] = mapped_column(Float)
    reviews_count: Mapped[int | None] = mapped_column(Integer)
    verified: Mapped[bool | None] = mapped_column(Boolean)
    is_company: Mapped[bool | None] = mapped_column(Boolean)
    description: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ads = relationship("Ad", back_populates="seller", cascade="all, delete-orphan")
    locations = relationship("Location", back_populates="seller", cascade="all, delete-orphan")
    services = relationship("Service", back_populates="seller", cascade="all, delete-orphan")
    parts = relationship("PartSale", back_populates="seller", cascade="all, delete-orphan")
    contacts = relationship("Contact", back_populates="seller", cascade="all, delete-orphan")
    ratings = relationship("SellerRating", back_populates="seller", cascade="all, delete-orphan")
    reviews = relationship("SellerReview", back_populates="seller", cascade="all, delete-orphan")


class Ad(Base):
    __tablename__ = "ads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    avito_id: Mapped[str | None] = mapped_column(String(64), unique=True, index=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    title: Mapped[str | None] = mapped_column(String(512))
    price: Mapped[int | None] = mapped_column(Integer, index=True)
    price_type: Mapped[str | None] = mapped_column(String(64))
    category: Mapped[str | None] = mapped_column(String(64), index=True)
    url: Mapped[str | None] = mapped_column(Text)
    image: Mapped[str | None] = mapped_column(Text)
    photos: Mapped[list[Any] | None] = mapped_column(JSON)
    address: Mapped[str | None] = mapped_column(String(512))
    coords: Mapped[str | None] = mapped_column(String(128))
    lat: Mapped[float | None] = mapped_column(Float)
    lon: Mapped[float | None] = mapped_column(Float)
    description: Mapped[str | None] = mapped_column(Text)
    params: Mapped[dict[str, Any] | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    seller = relationship("Seller", back_populates="ads")


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    name: Mapped[str | None] = mapped_column(String(255))
    address: Mapped[str | None] = mapped_column(String(512))
    lat: Mapped[float | None] = mapped_column(Float, index=True)
    lon: Mapped[float | None] = mapped_column(Float, index=True)
    coords: Mapped[str | None] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="locations")

class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    title: Mapped[str | None] = mapped_column(String(255))
    price: Mapped[int | None] = mapped_column(Integer)
    unit: Mapped[str | None] = mapped_column(String(64))
    category: Mapped[str | None] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="services")


class PartSale(Base):
    __tablename__ = "parts_sales"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    title: Mapped[str | None] = mapped_column(String(255))
    price: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="parts")


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    phone: Mapped[str | None] = mapped_column(String(64), index=True)
    type: Mapped[str | None] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="contacts")


class SellerRating(Base):
    __tablename__ = "seller_ratings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    rating: Mapped[float | None] = mapped_column(Float)
    reviews_count: Mapped[int | None] = mapped_column(Integer)
    source: Mapped[str | None] = mapped_column(String(64))
    fetched_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="ratings")


class SellerReview(Base):
    __tablename__ = "seller_reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seller_id: Mapped[int | None] = mapped_column(Integer, index=True)
    avito_review_id: Mapped[str | None] = mapped_column(String(128))
    author: Mapped[str | None] = mapped_column(String(128))
    rating: Mapped[int | None] = mapped_column(Integer)
    text: Mapped[str | None] = mapped_column(Text)
    date: Mapped[str | None] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    seller = relationship("Seller", back_populates="reviews")

