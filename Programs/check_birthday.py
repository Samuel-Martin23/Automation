from typing import List
from datetime import date
from automation_functions import send_notification


def check_date() -> None:
    i: int
    day: str
    today: str = date.today().strftime("%m/%d")
    birthday_texts: List[str] = []
    dates: List[str] = ["12/12"]
    names: List[str] = ["Name"]

    for i, day in enumerate(dates):
        if day == today:
            birthday_texts.append("Today is {}'s Birthday!".format(names[i]))

    if not birthday_texts:
        birthday_texts.append("No birthdays today.")

    for birthday in birthday_texts:
        send_notification("Birthday Update", birthday)


check_date()
print("Ran check_birthday.py")
