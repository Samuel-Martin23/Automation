#!/bin/bash 

#0 8 * * * cd ~/Desktop/Stuff/Automation/ && ./run.sh >/dev/null 2>&1

array_of_python_executables=()
while IFS='' read -r line; do array_of_python_executables+=("$line"); done < <(find /Users -name python)

for executable in "${array_of_python_executables[@]}"
do
  if [[ $executable == *"Automation"* ]]; then
    path_to_python_executable=$executable
    break
  fi
done

#Declaring Variables
path_to_check_slack_py=$(mdfind -name check_slack.py)
path_to_check_news_py=$(mdfind -name check_news.py)
path_to_check_quote_py=$(mdfind -name check_quote.py)
path_to_check_weather_py=$(mdfind -name check_weather.py)
path_to_check_call_py=$(mdfind -name check_call.py)
path_to_check_birthday_py=$(mdfind -name check_birthday.py)
send_notification="osascript -e 'display notification \"\" with title \"Ran Scripts\"'"

#Running programs
eval "$path_to_python_executable $path_to_check_slack_py"
eval "$path_to_python_executable $path_to_check_news_py"
eval "$path_to_python_executable $path_to_check_quote_py"
eval "$path_to_python_executable $path_to_check_weather_py"
eval "$path_to_python_executable $path_to_check_call_py"
eval "$path_to_python_executable $path_to_check_birthday_py"
eval "$send_notification"