import uuid
from backend.app.models.users import User


async def save_user(user_data):
    user = await User.get_or_none(username=user_data.username)
    if user:
        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.birthdate = user_data.birthdate
        user.time_left = user_data.time_left
        await user.save()
        return {"message": "Данные пользователя обновлены", "share_link": user.share_link}
    else:
        share_link = uuid.uuid4()
        await User.create(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            username=user_data.username,
            birthdate=user_data.birthdate,
            time_left=user_data.time_left,
            share_link=share_link,
        )
        return {"message": "Пользователь создан", "share_link": share_link}


async def get_user(share_link):
    user = await User.get_or_none(share_link=share_link)
    if user:
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "time_left": user.time_left,
        }
    else:
        return None
