from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse
from backend.app.core.settings import settings
from backend.app.schemas.schemas import UserData
from backend.app.services.date_service import calculate_time_until_birthday
from backend.app.services.user_service import get_user, save_user

router = APIRouter()


@router.get("/page_for/{username}")
async def web_app_by_username(username: str):
    web_app_url = f"{settings.get_vue_base_url}/web_page_for/{username}"
    return RedirectResponse(url=web_app_url)


@router.get("/birthday_counter/{birthdate}")
async def birthday_counter(birthdate: str):
    return calculate_time_until_birthday(birthdate)


@router.post("/save_user_data/")
async def save_user_data(user_data: UserData):
    try:
        result = await save_user(user_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_user_data/{share_link}")
async def get_user_data(share_link: str):
    try:
        user_data = await get_user(share_link)
        if user_data:
            return user_data
        else:
            return {"user": False}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
