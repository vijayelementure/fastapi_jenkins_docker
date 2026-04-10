from pydantic import BaseModel


class DeviceCreate(BaseModel):
    device_id: str


class DeviceData(BaseModel):
    device_id: str
    ph: float
    tds: float


class User(BaseModel):
    username: str
    password: str
