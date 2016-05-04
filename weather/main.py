import requests
import bs4
import collections

Weather_data = collections.namedtuple('Weather_data', 'condition, location, temp, units')

class ZipException(Exception):
    pass


def main():
    print_header()
    zipcode = get_zipcode()
    while True:
        try:
            weather = get_weather_data(zipcode)
        except ZipException as e:
            print("Invalid Zipcode", end='\n\n')
            continue
        else: break

    print("The weather in {} is {} {} and {}".format(weather.location, weather.temp, weather.units, weather.condition))


def print_header():
    print('--------------------------')
    print('       Weather App')
    print('--------------------------', end='\n\n')


def get_zipcode():
    return input("Enter a zipcode to get the weather forecast (ex. 48145): ").strip()


def get_weather_data(zipcode: str):
    html = get_weather_html(zipcode)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.find(id="location").find(class_='city-nav-header').text.strip().split('\n')[0]
    temp = soup.find(id='curTemp').find(class_='wx-value').text.strip()
    unit = soup.find(id='curTemp').find(class_='wx-unit').text.strip()
    cond = soup.find(id='curCond').find(class_='wx-value').text.strip()
    return Weather_data(cond, loc, temp, unit)

def get_weather_html(zipcode: str):
    response = requests.get('https://www.wunderground.com/weather-forecast/{}'.format(zipcode))
    if response.status_code != 200:
        raise ZipException

    return response.text



if __name__ == '__main__':
    main()

