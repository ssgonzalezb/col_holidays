from datetime import date as dt
import calc_easter_day
import fixed_holidays
import dinamic_holidays
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/isholiday/{date}")
async def isholiday(date: dt):
    try:
        if fixed_holidays.is_holiday(date) or dinamic_holidays.is_holiday(date):
            return {"message": f"The date {date} is holiday"}
        else:
            return {"message": f"The date {date} is not holiday"}
    except ValueError:
        return {"message": f"The date {date} is not valid"}


@app.get("/easter/{year}")
async def easter(year: int):
    try:
        return {"message": f"The easter day of {year} is {dinamic_holidays.calc_easter_day.easterCalc(year)}"}
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/fixedholidays/{year}")
async def fixedholidays(year: int):
    try:
        return fixed_holidays.fixed_holidays_by_year(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/dinamicholidays/{year}")
async def dinamicholidays(year: int):
    try:
        return dinamic_holidays.dinamic_holidays_by_year(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/easterdays/{year}")
async def easterdays(year: int):
    try:
        return calc_easter_day.easter_days(year)
    except ValueError:
        return {"message": f"The year {year} is not valid"}


@app.get("/holidays/{year}")
async def holidays(year: int):
    try:
        year_holidays = {}
        for x, y in fixed_holidays.fixed_holidays_by_year(year).items():
            year_holidays[x] = y

        for x, y in dinamic_holidays.dinamic_holidays_by_year(year).items():
            year_holidays[x] = y

        for x, y in calc_easter_day.easter_days(year).items():
            year_holidays[x] = y

        return dict(sorted(year_holidays.items()))
    except ValueError:
        return {"message": f"The year {year} is not valid"}