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
from webdriver_manager.firefox import GeckoDriverManager
from random import seed
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import random
import string
import names
import requests
import time

import simplejson as json

proxy = Proxy()
cur_proxy = proxy.proxy
options = Options()

driver = webdriver.Firefox()

options.add_argument(f"--proxy-server={cur_proxy} executable_path=GeckoDriverManager().install()")

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
    time.sleep(getRandomTime())
    register_btn = driver.find_element(By.CSS_SELECTOR, "._ab25 > a:nth-child(1)")
    register_btn.click()

def generate_email():
    json_email = requests.get(url = "https://www.guerrillamail.com/ajax.php?f=get_email_address&ip=127.0.0.1&agent=Mozilla_foo_bar")
    data = json.loads(json_email.text)
    email = data["email_addr"]
    return email

def generate_pass():
    length = random.randint(8, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Generates a string of random Charachters for the username
def generate_username():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(8, 16)))

def generate_legal_name():
    json_name = requests.get(url = "https://randomuser.me/api/")
    data = json.loads(json_name.text)
    name = f"{data['results'][0]['name']['first']} {data['results'][0]['name']['last']}"
    return name;

def input_info(email, password, real_name, user_name):
    try:
        email_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[4]/div/label/input")

    except:
        print("Email Field not found")
        return -1;

    try:
        pass_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[5]/div/label/input")
    except:
        print("Password field not found")
        return -1;
    
    try:
        full_name_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[6]/div/label/input")
    except:
        print("Full Name Field not found")
        return -1;

    try:
        username_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[7]/div/label/input")
    except:
        print("Username Field not found")
        return -1;

    try:
        register_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[8]/div/button")
    except:
        print("Registration Button not found")
        return -1;

    email_field.send_keys(email)
    pass_field.send_keys(password)
    full_name_field.send_keys(real_name)
    username_field.send_keys(user_name)

    register_btn.click()

    return 0

def getRandomTime():
    return randint(3, 5)

def main():
    proxy_get()
    #proxy_validate()
    webdriver_start()
    reject_cookies()
    click_register_btn()
    email = generate_email()
    password = generate_pass()
    real_name = generate_legal_name()
    user_name = generate_username()
    input_info(email, password, real_name, user_name)
    return 0

main()