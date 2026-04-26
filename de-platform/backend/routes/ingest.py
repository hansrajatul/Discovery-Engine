from fastapi import APIRouter
from db import SessionLocal
from models import LinuxAsset

router = APIRouter()

@router.post("/ingest/linux")
def ingest_linux(data: dict):
    db = SessionLocal()

    for user in data.get("users", []):
        asset = LinuxAsset(
            server=data["server"],
            username=user["username"],
            uid=int(user["uid"]),
            shell=user["shell"],
            is_sudo=user["username"] in data.get("sudo", "")
        )
        db.add(asset)

    db.commit()
    return {"status": "success"}
