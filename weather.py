import pyowm
import datetime
from pyowm.exceptions import api_response_error

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ua')

place = input('В якому місті/країні?: ')
try:
    observation = owm.weather_at_place(place)
    w = observation.get_weather()

    temp = w.get_temperature('celsius')["temp"]
    is_it_rain = w.get_status()

    today = datetime.datetime.today()
    if 0 <= today.hour <= 9:
        hour = '0' + str(today.hour)
    else:
        hour = str(today.hour)
    if 0 <= today.minute <= 9:
        minute = '0' + str(today.minute)
    else:
        minute = str(today.minute)
    print('Зараз', hour, ':', minute, sep=' ')
    if is_it_rain == 'Rain':
        print('В місті', place, 'зараз дощ')
    print('В місті', place, 'зараз', w.get_detailed_status())
    print('Темпаратура зараз приблизно', str(temp))

    if temp < 0:
        print('Зараз ппц як холодно, одягайся як танк!')
    elif temp < 10:
        print('Зараз холодно, одягнися тепліше.')
    elif temp < 20:
        print('Температура норм, одягай що завгодно.')
    else:
        print('Очманіти, як жарко! Одягайся якомога голіше!')
except api_response_error.NotFoundError:
    print('Wrong information, try again and find out mistakes please')
