from fastapi import APIRouter
from datetime import datetime, timedelta
from app.database import devices_collection

router = APIRouter()


@router.post("/register-device")
def register_device(data: dict):
    devices_collection.insert_one({
        "device_id": data["device_id"],
        "last_seen": None
    })
    return {"msg": "Device registered"}


@router.post("/send-data")
def send_data(data: dict):
    devices_collection.update_one(
        {"device_id": data["device_id"]},
        {"$set": {"last_seen": datetime.utcnow(),
                  "ph": data["ph"],
                  "tds": data["tds"]}}
    )
    return {"msg": "Data updated"}


@router.get("/status/{device_id}")
def device_status(device_id: str):
    device = devices_collection.find_one({"device_id": device_id})

    if not device or not device.get("last_seen"):
        return {"status": "inactive"}

    if datetime.utcnow() - device["last_seen"] > timedelta(minutes=10):
        return {"status": "inactive"}

    return {"status": "active"}
