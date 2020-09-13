from os import remove
from typing import List
from automation_functions import (sleep, get_driver, check_xpath_element, check_xpath_elements,
                                  send_notification, quit_chromium, webdriver, operating_system,
                                  user_name)
from xpaths_strings import (slack_workspace_label, slack_workspace, slack_workspace_button, username_label,
                            slack_email, password_label, slack_password, sign_in_button,
                            challenge_iv_channel_button, add_reaction_to_newest_post_button, search_emoji_label,
                            thumbs_up_button, reaction_bar_buttons, newest_post_slack_name)


def get_slack_update() -> None:
    driver.get("https://slack.com/signin")
    driver.set_window_size(1440, 700)

    check_xpath_element(driver, slack_workspace_label).send_keys(slack_workspace)
    check_xpath_element(driver, slack_workspace_button).click()

    check_xpath_element(driver, username_label).send_keys(slack_email)
    check_xpath_element(driver, password_label).send_keys(slack_password)

    check_xpath_element(driver, sign_in_button).click()
    check_xpath_element(driver, channel_button).click()

    thumbs_up_the_post()


def thumbs_up_the_post() -> None:
    if not check_post_reaction() and check_slack_name():
        check_xpath_element(driver, add_reaction_to_newest_post_button).click()
        check_xpath_element(driver, search_emoji_label).send_keys("thumbsup")
        check_xpath_element(driver, thumbs_up_button).click()

    if operating_system() == "Windows":
        path_to_screenshot: str = f"C:\\Users\\{user_name()}\\Desktop\\slack_post.png"
    else:
        path_to_screenshot: str = f"/Users/{user_name()}/Desktop/slack_post.png"
    driver.get_screenshot_as_file(path_to_screenshot)
    sleep(4)
    send_notification("Slack Update", "Post", path_to_screenshot)
    quit_chromium(driver)
    remove(path_to_screenshot)


def check_post_reaction() -> bool:
    reactions: List[webdriver.remote] = check_xpath_elements(driver, reaction_bar_buttons)

    if not reactions:
        return True

    for react in reactions:
        if react.get_attribute("aria-pressed") == "true":
            return True
    return False


def check_slack_name() -> bool:
    if check_xpath_element(driver, newest_post_slack_name).text == "USER":
        return True
    else:
        return False


driver: webdriver = get_driver()
get_slack_update()
print("Ran check_slack.py")
