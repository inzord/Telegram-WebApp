from datetime import datetime
from fastapi import HTTPException


def calculate_time_until_birthday(birthdate: str):
    try:
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        next_birthday = birthdate.replace(year=current_date.year)

        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)

        time_left = datetime.combine(next_birthday, datetime.min.time()) - datetime.now()

        if time_left.total_seconds() < 0:
            return {"message": "День рождения сегодня"}

        days_left = time_left.days
        hours_left, remainder = divmod(time_left.seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)

        return {"until_birthday": f"Дней: {days_left}, часов: {hours_left}, минут: {minutes_left}"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректный формат даты. Используйте ГГГГ-ММ-ДД")
