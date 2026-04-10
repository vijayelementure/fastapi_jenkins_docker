from pydantic import BaseModel
from datetime import datetime


class Device(BaseModel):
    device_id: str
    timestamp: datetime
    ph: float
    tds: float
