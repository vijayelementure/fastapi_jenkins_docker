from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.utils.auth import hash_password, verify_password, create_token
from app.schemas import User
router = APIRouter()


@router.post("/register")
def register(user: User):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    users_collection.insert_one(user_dict)
    return {"msg": "User created"}


@router.post("/login")
def login(user: User):
    db_user = users_collection.find_one({"username": user.username})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"username": user.username})
    return {"access_token": token}
