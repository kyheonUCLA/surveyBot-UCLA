import imp
from os import error
import os
import time
import json
from dotenv import load_dotenv

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException        


def login(driver, username, password):
    driver.find_element(By.ID, "logon").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "_eventId_proceed").click()
    print('Done')


def element_exists(driver, method, key):
    try:
        driver.find_element(method, key)
    except NoSuchElementException:
        return False
    return True

url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7"
driver = webdriver.Chrome('driver/chromedriver')
driver.get(url)


username = None
password = None
with open('keys.json', 'r') as ifile:
    data = json.loads(ifile.read())
    username = data['username']
    password = data['password']

time.sleep(2)
btn = driver.find_element(By.ID, "QID3-2-label")
btn.click()
btn = driver.find_element(By.ID, "NextButton")
btn.click()
time.sleep(2)

login(driver, username, password)
#os.environ.clear()

time.sleep(1)
iframe = driver.find_element(By.ID, 'duo_iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="auth_methods"]/fieldset[1]/div[1]/button').click()
driver.switch_to.default_content()

timeout = 0
while True:
    if timeout >= 30 or element_exists(driver, By.ID, 'NextButton'):
        break
    time.sleep(1)
    timeout = timeout + 1


ID_LABELS = ['QID215-1-label', 'QID239-12-label', 'QID207-4-label',  'QID2-1-label', 'QID12-2-label', 'QID289-2-label', 'QID293-1-label']

driver.find_element(By.ID, 'NextButton').click()
time.sleep(1)
driver.find_element(By.ID, 'NextButton').click()
time.sleep(1)

for id in ID_LABELS:
    time.sleep(1)
    driver.find_element(By.ID, id).click()
    driver.find_element(By.ID, 'NextButton').click()

