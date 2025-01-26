"""
Pseudo-code:
    0. Connect to random proxy X
    1. Open Web Browser
    2. Go to "https://www.instagram.com/accounts/emailsignup/"
    3. Reject cookies
    4. Call tempmail API
        4.1. Get an email address
    5. Generate a random password string
    6. Generate a random human Name
    7. Generate a random username
    8. Click next
    9. Click birth year dropdown
    10. Select a random year 18 or more years in the past
    11. Click next
    12. Wait for email-message
    13. Once detected, scan the email string for a 6 number combination
    14. Click next
    15. If banned, refresh proxy and retry steps 1 to 14
    16. Go to the profile url
    17. Click follow
    18. Refresh webpage
    19. Click button to view all reccomended
    20. Recopile profile urls and save them in a file
"""

from proxy import Proxy
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import random
import string
import names
import requests

proxy = Proxy()
cur_proxy = proxy.proxy
options = Options()

driver = webdriver.Firefox()

options.add_argument(f"--proxy-server={cur_proxy}")

def proxy_get():
    proxy.cycle()

    while proxy.test_proxy(cur_proxy) != 0:
        print("Failed to connect to proxy. Trying with another proxy...")

        if proxy.cycle() == 0:
            print("Could not find a valid proxy")
            return -1

    print("Succesfully connected to proxy")
    print("")
    return 0

def proxy_validate():
    proxy = Proxy(validate_proxies=True)

def webdriver_start():
    driver.get("https://www.instagram.com")

def reject_cookies():
    cookies_btn = driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(3)")
    cookies_btn.click()

def click_register_btn():
    register_btn = driver.find_element(By.CSS_SELECTOR, "._ab25 > a:nth-child(1)")
    register_btn.click()

def generate_email():
    email = requests.get(url = "https://1secmail.pro/api/email/")
    return email

def generate_pass():
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Generates a string of random Charachters for the username
def generate_username():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randintb(8, 16)))

def input_info(email, password, real_name, user_name):
    register_btn = driver.findElement(By.className("x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"))

    email_field = driver.findElement(By.className("_aa4b _add6 _ac4d _ap35"))
    pass_field = driver.findElement(By.className("_aa4b _add6 _ac4d _ap35"))
    full_name_field = driver.findElement(By.className("_aa4b _add6 _ac4d _ap35"))
    username_field = driver.findElement(By.className("_aa4b _add6 _ac4d _ap35"))

    email_field.sendKeys(email)
    pass_field.sendKeys(password)
    full_name_field.sendKeys(real_name)
    username_field.sendKeys(user_name)

    return 0


def main():
    proxy_get()
    #proxy_validate()
    webdriver_start()
    reject_cookies()
    click_register_btn()
    email = generate_email()
    password = generate_pass()
    real_name = names()
    user_name = generate_username()
    return 0

main()