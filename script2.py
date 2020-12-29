import requests

API = '1dfd75256515118b98659e8282a0371e'
# URL = f'http://api.openweathermap.org/data/2.5/weather?id={id}&lang=ru&units=metric&appid={API}'
URL = f'https://api.openweathermap.org/data/2.5/onecall?lat=55.761665&lon=-37.606667&units=metric&exclude=hourly&appid={API}'


def get_data(url):
    r = requests.get(url)
    return r


def get_avg_temp(url):
    response = get_data(url)
    response = response.json().get('daily')
    temp_list = []
    ctr = 0
    for i in response:
        temp_list.append(i['feels_like']['eve'])
        ctr += 1
        if ctr == 6:
            break
    return sum(temp_list) / len(temp_list)


def get_min_pres(url):
    response = get_data(url)
    response = response.json().get('daily')
    pres_list = []
    for i in response:
        pres_list.append(i['pressure'])
    return min(pres_list)


if __name__ == '__main__':
    print(f'The average temperature in Moscow: {get_avg_temp(URL)} ℃')
    print(f'The minimal pressure in Moscow: {get_min_pres(URL)} hPa')
