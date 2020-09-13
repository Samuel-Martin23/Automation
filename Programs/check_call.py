from typing import List
from random import randint
from datetime import datetime
from automation_functions import (send_notification, sys_output, user_name, operating_system)


def check_call() -> None:
    name_of_today: str = datetime.now().strftime("%A")
    if name_of_today == "Friday":
        if operating_system() == "Windows":
            path_to_call_list: str = sys_output(f"cd \\Users\\{user_name()} && dir /s /b people_to_call.txt")
        else:
            path_to_call_list: str = sys_output("mdfind", "-name", "people_to_call.txt")

        with open(path_to_call_list, "r") as file:
            names: List[str] = file.readlines()

        who_to_call: int = randint(0, len(names) - 1)

        send_notification("Person to call", names[who_to_call].strip())

        names.remove(names[who_to_call])

        if not names:
            names = ["Name\n"]

        with open(path_to_call_list, "w") as file:
            for name in names:
                file.write(name)


check_call()
print("Ran check_call.py")
