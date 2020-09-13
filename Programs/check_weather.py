from automation_functions import (get_driver, check_xpath_element, send_notification, webdriver)
from xpaths_strings import (google_search_label, google_weather_type_label, google_high_temp_label,
                            google_low_temp_label, google_precipitation_label, google_humidity_label,
                            google_wind_label)


def get_weather(zip_code: str) -> None:
    RETURN_KEY: str = "\ue006"
    check_xpath_element(driver, google_search_label).send_keys("weather " + zip_code)
    check_xpath_element(driver, google_search_label).send_keys(RETURN_KEY)

    weather_type: str = "Weather: " + check_xpath_element(driver, google_weather_type_label).text.title() + "\n"

    high_temperature: str = check_xpath_element(driver, google_high_temp_label).text
    high_temperature = 'High Temperature: <font color="{}">{}</font>°F\n'.format(
        get_temp_color(int(high_temperature)), high_temperature)

    low_temperature: str = check_xpath_element(driver, google_low_temp_label).text
    low_temperature = 'Low Temperature: <font color="{}">{}</font>°F\n'.format(
        get_temp_color(int(low_temperature)), low_temperature)

    precipitation: str = check_xpath_element(driver, google_precipitation_label).text.split("%")[0]
    precipitation = 'Precipitation: <font color="{}">{}</font>%\n'.format("#5d96d4", precipitation)

    humidity: str = check_xpath_element(driver, google_humidity_label).text.split("%")[0]
    humidity = 'Humidity: <font color="{}">{}</font>%\n'.format("#28b319", humidity)

    wind: str = check_xpath_element(driver, google_wind_label).text.split(" ")[0]
    wind = 'Wind: <font color="{}">{}</font> MPH\n'.format("#d1fffd", wind)

    total_weather_report: str = weather_type + high_temperature + low_temperature + precipitation + humidity + wind
    send_notification(f"Weather Report from {zip_code}", total_weather_report)


def get_temp_color(temp: int) -> str:
    if temp >= 90:
        return "#ff1400"
    elif 70 <= temp < 90:
        return "#8fdbeb"
    else:
        return "#007bff"


driver: webdriver = get_driver()
driver.get("https://www.google.com/")
get_weather("ZIP_CODE")
print("Ran check_weather.py")
