from fastapi import FastAPI
from app.routes import device, auth

app = FastAPI()

app.include_router(device.router, prefix="/device")
app.include_router(auth.router, prefix="/auth")


@app.get("/")
def root():
    return {"msg": "API Running"}
