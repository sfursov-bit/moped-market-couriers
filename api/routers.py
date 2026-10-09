from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from api.schemas import Point, SellerDetail
from db.session import get_session
from models import models

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/points", response_model=list[Point])
async def points(city: str | None = Query(default=None), category: str | None = Query(default=None), search: str | None = Query(default=None), session: Session = Depends(get_session)):
    q = select(models.Ad).join(models.Seller).options(joinedload(models.Ad.seller))
    if city:
        q = q.where(models.Seller.city.ilike(f"%{city}%"))
    if category:
        q = q.where(models.Ad.category == category)
    if search:
        q = q.where(models.Ad.title.ilike(f"%{search}%"))
    ads = session.execute(q).scalars().all()
    out = []
    for a in ads:
        if a.lat is None or a.lon is None:
            continue
        out.append(Point(id=a.id, avito_id=a.avito_id, lat=a.lat, lon=a.lon, title=a.title, price=a.price, category=a.category, url=a.url, seller_name=a.seller.name if a.seller else None, city=a.seller.city if a.seller else a.city))
    return out

from __future__ import annotations

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from api.schemas import SellerDetail
from api.routers import router
from db.session import get_session
from models import models

@router.get("/sellers/{seller_id}", response_model=SellerDetail)
async def seller_detail(seller_id: int, session: Session = Depends(get_session)):
    s = session.execute(select(models.Seller).options(joinedload(models.Seller.ads), joinedload(models.Seller.locations), joinedload(models.Seller.services), joinedload(models.Seller.parts), joinedload(models.Seller.contacts)).where(models.Seller.id == seller_id)).scalar_one_or_none()
    if not s:
        raise HTTPException(404, "seller not found")
    return SellerDetail(id=s.id, avito_id=s.avito_id, name=s.name, city=s.city, url=s.url, avatar=s.avatar, rating=s.rating, reviews_count=s.reviews_count, description=s.description, locations=[{"id":l.id,"name":l.name,"address":l.address,"lat":l.lat,"lon":l.lon} for l in s.locations], services=[{"id":sv.id,"title":sv.title,"price":sv.price,"unit":sv.unit} for sv in s.services], parts=[{"id":p.id,"title":p.title,"price":p.price} for p in s.parts], contacts=[{"id":c.id,"phone":c.phone,"type":c.type} for c in s.contacts], ads=[{"id":a.id,"title":a.title,"price":a.price,"category":a.category,"url":a.url} for a in a.ads] if False else [])

