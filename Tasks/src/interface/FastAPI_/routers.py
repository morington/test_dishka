from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def ping() -> str:
    return "pong"