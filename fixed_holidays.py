import datetime

"""
Function to return fixed Colombian holidays for a given year
"""
def fixed_holidays_by_year(year):
    fixed_holidays = {datetime.date(year, 1, 1): "Año Nuevo",
                      datetime.date(year, 5, 1): "Día del Trabajo",
                      datetime.date(year, 7, 20): "Grito de Independencia",
                      datetime.date(year, 8, 7): "Batalla de Boyacá",
                      datetime.date(year, 12, 8): "Día de la Inmaculada Concepción",
                      datetime.date(year, 12, 25): "Navidad"}
    return fixed_holidays

def fixed_holidays_by_date(date):
    fixed_holidays = {datetime.date(date.year, 1, 1): "Año Nuevo",
                      datetime.date(date.year, 5, 1): "Día del Trabajo",
                      datetime.date(date.year, 7, 20): "Grito de Independencia",
                      datetime.date(date.year, 8, 7): "Batalla de Boyacá",
                        datetime.date(date.year, 12, 8): "Día de la Inmaculada Concepción",
                        datetime.date(date.year, 12, 25): "Navidad"}
    return fixed_holidays

def is_holiday(date):
    if date in fixed_holidays_by_date(date):
        return True