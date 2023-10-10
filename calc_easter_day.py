from datetime import date, timedelta

"""
Function to calculate the Easter Day of a given year post 1583 using the Butcher algorithm
Source: https://es.wikipedia.org/wiki/Computus#Algoritmo_de_Butcher
"""


def easter_calc(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = h + l - 7 * m + 114
    month = n // 31
    day = 1 + (n - (month * 31))

    return date(year, month, day)


def easter_days(year: int):
    easter = easter_calc(year)
    easter_holidays = {easter - timedelta(days=3): "Jueves santo",
                       easter - timedelta(days=2): "Viernes santo",
                       easter + timedelta(days=43): "Ascension de Jesus",
                       easter + timedelta(days=64): "Corpus Christi",
                       easter + timedelta(days=71): "Sagrado Corazon"}

    return easter_holidays
