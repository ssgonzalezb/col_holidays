from datetime import date as dt
import calc_easter_day
import fixed_holidays
import dynamic_holidays
from fastapi import FastAPI

app = FastAPI()


@app.get("/is_holiday/{date}")
async def isholiday(date: dt):
    try:
        if fixed_holidays.is_holiday(date) or dynamic_holidays.is_holiday(date):
            return True

        return False

    except ValueError:
        return {"message": f"The date {date} is not valid"}


@app.get("/easter/{year}")
async def easter(year: int):
    try:
        return {"Easter day": calc_easter_day.easter_calc(year)}
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/fixed_holidays/{year}")
async def get_fixed_holidays(year: int):
    try:
        return fixed_holidays.fixed_holidays(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/dynamic_holidays/{year}")
async def get_dynamic_holidays(year: int):
    try:
        return dynamic_holidays.dynamic_holidays(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/easter_days/{year}")
async def get_easter_days(year: int):
    try:
        return calc_easter_day.easter_days(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/holidays/{year}")
async def get_holidays(year: int):
    try:
        year_holidays = {}
        for x, y in fixed_holidays.fixed_holidays(year).items():
            year_holidays[x] = y

        for x, y in dynamic_holidays.dynamic_holidays(year).items():
            year_holidays[x] = y

        for x, y in calc_easter_day.easter_days(year).items():
            year_holidays[x] = y

        return dict(sorted(year_holidays.items()))
    except ValueError:
        return {"message": f"The year {year} is not valid"}
