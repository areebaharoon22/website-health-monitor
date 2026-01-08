'''
Docstring for website health monitor (simple version)
Name: Areeba Haroon
Date: 1/1/2026
Purpose: This program checks any url's health (up or down) and logs it to a file. 
'''
import requests
import time
from datetime import datetime


CHECK_INTERVAL = 60  # seconds
LOG_FILE = "health.log"

def check_website(URL_TO_CHECK):
    try:
        start_time = time.time()
        response = requests.get(URL_TO_CHECK, timeout=5)
        response_time = round(time.time() - start_time, 2)

        status = "UP" if response.status_code == 200 else "DOWN"
        log_message = (
            f"{datetime.now()} | {URL_TO_CHECK} | {status} | "
            f"Status Code: {response.status_code} | Response Time: {response_time}s"
        )

    except Exception as error:
        status = "DOWN"
        log_message = (
            f"{datetime.now()} | {URL_TO_CHECK} | DOWN | Error: {error}"
        )

    print(log_message)
    if status == "DOWN":
        print("ALERT: Website is DOWN!")


    with open(LOG_FILE, "a") as file:
        file.write(log_message + "\n")


if __name__ == "__main__":
    print("Starting website health monitor...\n")
    URL_TO_CHECK = input("Please enter your url to check it\'s health: ") # i.e. "https://www.google.com"
    try:
        while True:
            check_website(URL_TO_CHECK)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
