from datetime import date

"""
Function to return fixed Colombian holidays for a given year
"""


def fixed_holidays(year):
    lst_fixed_holidays = {date(year, 1, 1): 'Año Nuevo',
                          date(year, 5, 1): 'Día del Trabajo',
                          date(year, 7, 20): 'Grito de Independencia',
                          date(year, 8, 7): 'Batalla de Boyaca',
                          date(year, 12, 8): 'Dia de la Inmaculada Concepcion',
                          date(year, 12, 25): "Navidad"}
    return lst_fixed_holidays


def is_holiday(dt: date):
    if dt in fixed_holidays(dt.year):
        return True

    return False
