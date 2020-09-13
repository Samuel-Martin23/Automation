import platform
from getpass import getuser
from typing import (Union, List)
from subprocess import (Popen, PIPE, run)


def main() -> None:
    user_name: str = getuser()
    path_to_python_exe: str = get_path_to_python_exe(user_name)

    # Declaring Variables
    path_to_check_slack_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_slack.py")
    path_to_check_news_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_news.py")
    path_to_check_quote_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_quote.py")
    path_to_check_weather_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_weather.py")
    path_to_check_call_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_call.py")
    path_to_check_birthday_py: str = sys_output(f"cd \\Users\\{user_name} && dir /s /b check_birthday.py")

    # Running programs
    run([path_to_python_exe, path_to_check_slack_py], shell=True)
    run([path_to_python_exe, path_to_check_news_py], shell=True)
    run([path_to_python_exe, path_to_check_quote_py], shell=True)
    run([path_to_python_exe, path_to_check_weather_py], shell=True)
    run([path_to_python_exe, path_to_check_call_py], shell=True)
    run([path_to_python_exe, path_to_check_birthday_py], shell=True)

    exit()


def sys_output(cmd: str) -> Union[str, List[str]]:
    p: Popen = Popen(cmd, shell=True, stdout=PIPE)
    output: List[str] = p.communicate()[0].decode("ascii").strip().split("\n")
    if len(output) == 1:
        return output[0]
    else:
        return output


def get_path_to_python_exe(user) -> str:
    for path in sys_output(f"cd /Users/{user} && dir /s /b python.exe"):
        if "Automation" in path:
            return path


if platform.system() == "Windows":
    main()
else:
    print("Only for Windows.")
