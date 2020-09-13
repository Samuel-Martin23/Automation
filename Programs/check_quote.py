from typing import Dict
from automation_functions import (get_driver, scroll_down, check_xpath_element, send_notification, quit_chromium,
                                  webdriver)
from xpaths_strings import (bq_day_quote, bq_love_quote, bq_art_quote, bq_nature_quote, bq_funny_quote)


def get_quotes() -> None:
    driver.get("https://www.brainyquote.com/quote_of_the_day")
    quotes: Dict[str, str] = {}
    title: str
    text: str

    scroll_down(driver)
    quotes["Quote of the day"] = check_xpath_element(driver, bq_day_quote).text.replace("\n", " - ")

    scroll_down(driver)
    quotes["Love Quote of the day"] = check_xpath_element(driver, bq_love_quote).text.replace("\n", " - ")

    scroll_down(driver)
    quotes["Art Quote of the Day"] = check_xpath_element(driver, bq_art_quote).text.replace("\n", " - ")

    scroll_down(driver)
    quotes["Nature Quote of the Day"] = check_xpath_element(driver, bq_nature_quote).text.replace("\n", " - ")

    scroll_down(driver)
    quotes["Funny Quote Of the Day"] = check_xpath_element(driver, bq_funny_quote).text.replace("\n", " - ")

    quit_chromium(driver)

    for title, text in quotes.items():
        send_notification(title, text)


driver: webdriver = get_driver()
get_quotes()
print("Ran check_quote.py")
