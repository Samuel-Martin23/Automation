from typing import Dict
from automation_functions import (get_driver, check_xpath_element, send_notification, quit_chromium, webdriver)
from xpaths_strings import (google_search_label, google_news_tab, google_first_article_link,
                            google_first_article_name)


def get_news_article(search: str) -> None:
    driver.get("https://www.google.com/")
    RETURN_KEY: str = "\ue006"
    check_xpath_element(driver, google_search_label).send_keys(search)
    check_xpath_element(driver, google_search_label).send_keys(RETURN_KEY)
    check_xpath_element(driver, google_news_tab).click()

    article_title: str = check_xpath_element(driver, google_first_article_name).text
    article_link: str = check_xpath_element(driver, google_first_article_link).get_attribute("href")
    news_articles[article_title] = article_link


driver: webdriver = get_driver()
news_articles: Dict[str, str] = {}
title: str
link: str
get_news_article("abc breaking news")
get_news_article("nbc breaking news")
get_news_article("cnn breaking news")
get_news_article("coding")
get_news_article("programming")

quit_chromium(driver)

for title, link in news_articles.items():
    send_notification(f"News: {title}", f"<font color=#2868ac><u>{link}</u></font>")

print("Ran check_news.py")
