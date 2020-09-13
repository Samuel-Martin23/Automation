from time import sleep
from requests import post
from platform import system
from getpass import getuser
from selenium import webdriver
from subprocess import (Popen, PIPE, run)
from xpaths_strings import (user_token, user_key)
from selenium.webdriver.chrome.options import Options
from typing import (Dict, Tuple, BinaryIO, Union, List)
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver() -> webdriver:
    """
    https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html
    Search for LAST_CHANGE
    """
    chrome_options: webdriver.chrome.options.Options = Options()
    chrome_options.headless = True
    if operating_system() == "Windows":
        path_to_script: str = sys_output(f"cd \\Users\\{user_name()} && dir /s /b chromedriver.exe")
        chrome_options.binary_location = sys_output(f"cd \\Users\\{user_name()} && dir /s /b chromium.exe")
    else:
        path_to_script: str = sys_output("mdfind", "-name", "chromium_selenium")
        chrome_options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"
    return webdriver.Chrome(path_to_script, options=chrome_options)


def check_xpath_element(driver: webdriver, xpath: str, wait_time: float = 10) -> webdriver.remote:
    element = None
    try:
        element: webdriver.remote = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located(("xpath", xpath)))
    except TimeoutException:
        print("\nElement(By.XPATH" + ", " + xpath + ") does not exist or is out of reach.")
        exit(1)

    sleep(0.5)
    return element


def check_xpath_elements(driver: webdriver, xpath: str, wait_time: float = 10) -> webdriver.remote:
    elements = None
    try:
        elements: webdriver.remote = WebDriverWait(driver, wait_time).until(
            EC.presence_of_all_elements_located(("xpath", xpath)))
    except TimeoutException:
        print("\nElements(By.XPATH" + ", " + xpath + ") does not exist or is out of reach.")
        exit(1)

    sleep(0.5)
    return elements


def send_notification(title_text_message: str, body_text_message: str, image_path: str = "") -> None:
    image_file: Dict[str, Tuple[str, BinaryIO, str]] = {}

    if image_path:
        image_file = {"attachment": ("image.jpg", open(image_path, "rb"), "image/jpeg")}

    post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": user_token,
            "user": user_key,
            "html": 1,
            "title": title_text_message,
            "message": body_text_message
        },
        files=image_file
    )

    sleep(2)


def scroll_down(driver: webdriver, scroll_value: float = 325) -> None:
    sleep(0.5)
    driver.execute_script("window.scrollTo(0, window.scrollY + {});".format(scroll_value))
    sleep(0.5)


def quit_chromium(driver: webdriver) -> None:
    driver.quit()
    if operating_system() != "Windows":
        run(['osascript', '-e', 'quit app \"Chromium\"'])


def operating_system() -> str:
    return system()


def user_name() -> str:
    return getuser()


def sys_output(*cmd: str) -> Union[str, List[str]]:
    if operating_system() == "Windows":
        p: Popen = Popen(cmd[0], shell=True, stdout=PIPE)
    else:
        p: Popen = Popen(cmd, stdout=PIPE)
    output: List[str] = p.communicate()[0].decode("ascii").strip().split("\n")
    if len(output) == 1:
        return output[0]
    else:
        return output
