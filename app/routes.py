from fastapi import APIRouter, HTTPException
from .models import Item
from .database import get_redis_connection

router = APIRouter()

@router.post("/write_data")
async def write_data(item: Item):
    r = get_redis_connection()
    r.set(item.phone, item.address)
    return {"message": "Data saved successfully"}

@router.get("/check_data")
async def check_data(phone: str):
    r = get_redis_connection()
    address = r.get(phone)
    if not address:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {"phone": phone, "address": address}
