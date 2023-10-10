from datetime import date as dt, timedelta
import calc_easter_day

"""
Function to return dynamic Colombian holidays for a given year
Dynamic holidays aka "Ley Emiliani" are holidays that are moved to the next monday if they fall on a business day
Ley 51 de 1983 
"""


def dynamic_holidays(year: int):
    base_dynamic_holidays = {dt(year, 1, 6): "Reyes Magos", dt(year, 3, 19): "San José",
                             dt(year, 6, 29): "San Pedro y San Pablo",
                             dt(year, 8, 15): "Asunción de la Virgen",
                             dt(year, 10, 12): "Día de la Raza", dt(year, 11, 1): "Todos los Santos",
                             dt(year, 11, 11): "Independencia de Cartagena"}

    dynamic_holidays = {}

    for x, y in base_dynamic_holidays.items():
        current_x = dt(year, x.month, x.day)
        # Si la fecha está en la base de festivos variables y corresponde a un lunes
        if current_x.strftime('%w') == '1':
            dynamic_holidays[current_x] = y
        else:
            # Si la fecha está en la base de festivos variables y no corresponde a un lunes, trasladar al lunes siguiente
            # Se utiliza el método strftime con el formato %w para obtener el día de la semana (0 = domingo, 6 = sabado)
            # Se utiliza el metodo timedelta para sumar días a la fecha dada
            match current_x.strftime('%w'):
                case '0':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=1))
                    dynamic_holidays[current_x + timedelta(days=1)] = y
                case '2':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=6))
                    dynamic_holidays[current_x + timedelta(days=6)] = y
                case '3':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=5))
                    dynamic_holidays[current_x + timedelta(days=5)] = y
                case '4':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=4))
                    dynamic_holidays[current_x + timedelta(days=4)] = y
                case '5':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=3))
                    dynamic_holidays[current_x + timedelta(days=3)] = y
                case '6':
                    # dinamic_holidays.append(current_x + datetime.timedelta(days=2))
                    dynamic_holidays[current_x + timedelta(days=2)] = y

    return dynamic_holidays


def is_holiday(date: dt):
    easter_holidays = calc_easter_day.easter_days(date.year)
    lst_dynamic_holidays = dynamic_holidays(date.year)

    if date in lst_dynamic_holidays or date in easter_holidays:
        return True

    return False