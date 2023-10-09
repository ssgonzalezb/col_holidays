import datetime
import calc_easter_day

"""
Function to return dinamic Colombian holidays for a given year
Dinamic holidays aka "Ley Emiliani" are holidays that are moved to the next monday if they fall on a business day
Ley 51 de 1983 
"""
def dinamic_holidays(date: datetime):
    base_dinamic_holidays = [datetime.date(date.year,1,6), datetime.date(date.year,3,19), datetime.date(date.year,6,29),
                               datetime.date(date.year,8,15), datetime.date(date.year,10,12), datetime.date(date.year,11,1),
                               datetime.date(date.year,11,11), datetime.date(date.year, 12, 25)]

    dinamic_holidays = []

    for x in base_dinamic_holidays:
        current_x = datetime.date(date.year, x.month, x.day)
        #Si la fecha está en la base de festivos variables y corresponde a un lunes
        if current_x.strftime('%w') == '1':
            dinamic_holidays.append(current_x)
        else:
        #Si la fecha está en la base de festivos variables y no corresponde a un lunes, trasladar al lunes siguiente
        #Se utiliza el método strftime con el formato %w para obtener el día de la semana (0 = domingo, 6 = sabado)
        #Se utiliza el metodo timedelta para sumar días a la fecha dada
            match current_x.strftime('%w'):
                case '0':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=1))
                case '2':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=6))
                case '3':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=5))
                case '4':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=4))
                case '5':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=3))
                case '6':
                    dinamic_holidays.append(current_x + datetime.timedelta(days=2))

    return dinamic_holidays

def dinamic_holidays_by_year(year: int):
    base_dinamic_holidays = [datetime.date(year,1,6), datetime.date(year,3,19), datetime.date(year,6,29),
                             datetime.date(year,8,15), datetime.date(year,10,12), datetime.date(year,11,1),
                             datetime.date(year,11,11)]

    dict_base_dinamic_holidays = {datetime.date(year,1,6): "Reyes Magos", datetime.date(year,3,19): "San José",
                                  datetime.date(year,6,29): "San Pedro y San Pablo", datetime.date(year,8,15): "Asunción de la Virgen",
                                  datetime.date(year,10,12): "Día de la Raza", datetime.date(year,11,1): "Todos los Santos",
                                  datetime.date(year,11,11): "Independencia de Cartagena"}

    dinamic_holidays = {}

    for x, y in dict_base_dinamic_holidays.items():
        current_x = datetime.date(year, x.month, x.day)
        #Si la fecha está en la base de festivos variables y corresponde a un lunes
        if current_x.strftime('%w') == '1':
            dinamic_holidays[current_x] = y
        else:
            #Si la fecha está en la base de festivos variables y no corresponde a un lunes, trasladar al lunes siguiente
            #Se utiliza el método strftime con el formato %w para obtener el día de la semana (0 = domingo, 6 = sabado)
            #Se utiliza el metodo timedelta para sumar días a la fecha dada
            match current_x.strftime('%w'):
                case '0':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=1))
                    dinamic_holidays[current_x + datetime.timedelta(days=1)] = y
                case '2':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=6))
                    dinamic_holidays[current_x + datetime.timedelta(days=6)] = y
                case '3':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=5))
                    dinamic_holidays[current_x + datetime.timedelta(days=5)] = y
                case '4':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=4))
                    dinamic_holidays[current_x + datetime.timedelta(days=4)] = y
                case '5':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=3))
                    dinamic_holidays[current_x + datetime.timedelta(days=3)] = y
                case '6':
                    #dinamic_holidays.append(current_x + datetime.timedelta(days=2))
                    dinamic_holidays[current_x + datetime.timedelta(days=2)] = y

    return dinamic_holidays

def is_holiday(date: datetime):
    easter = calc_easter_day.easterCalc(date.year)
    arr_easter_holidays = []
    for x in dinamic_holidays(date):
        arr_easter_holidays.append(easter - datetime.timedelta(days=3)) #Jueves santo
        arr_easter_holidays.append(easter - datetime.timedelta(days=2)) #Viernes santo
        arr_easter_holidays.append(easter + datetime.timedelta(days=43)) #Ascension de Jesus
        arr_easter_holidays.append(easter + datetime.timedelta(days=64)) #Corpus Christi
        arr_easter_holidays.append(easter + datetime.timedelta(days=71)) #Sagrado Corazon

    if date in dinamic_holidays(date) or date in arr_easter_holidays:
        return True