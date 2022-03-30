from os import error
import time
import json
#from dotenv import load_dotenv

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException        


def wait(driver, method, key, timeout):
    count = 0
    while True:
        if element_exists(driver, method, key):
            break
        elif count > timeout:
            break
        time.sleep(0.25)
        count = count + 0.25

def login(driver, username, password):
    driver.find_element(By.ID, "logon").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "_eventId_proceed").click()
    print('Done Logging In')


def element_exists(driver, method, key):
    try:
        driver.find_element(method, key)
    except NoSuchElementException:
        return False
    return True

def main():
    url = "https://uclasurveys.co1.qualtrics.com/jfe/form/SV_3qRLtouCYKzBbH7"
    driver = webdriver.Chrome('drivers/chromedriver100')
    driver.get(url)


    username = None
    password = None
    with open('key.json', 'r') as ifile:
        data = json.loads(ifile.read())
        username = data['username']
        password = data['password']

    wait(driver, By.ID, "NextButton", 50)
    btn = driver.find_element(By.ID, "QID3-2-label")
    btn.click()
    btn = driver.find_element(By.ID, "NextButton")
    btn.click()
    
    wait(driver, By.ID, "pass", 50)
    login(driver, username, password)

    wait(driver, By.ID, "duo_iframe", 50)
    iframe = driver.find_element(By.ID, 'duo_iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, '//*[@id="auth_methods"]/fieldset[1]/div[1]/button').click()
    driver.switch_to.default_content()


    wait(driver, By.ID, 'NextButton', 50)
    driver.find_element(By.ID, 'NextButton').click()
    time.sleep(1) #using wait() breaks it here
    driver.find_element(By.ID, 'NextButton').click()

    ID_LABELS = ['QID215-1-label', 'QID239-12-label', 'QID207-4-label',  'QID2-1-label', 'QID12-2-label', 'QID289-2-label', 'QID293-1-label']

    for id in ID_LABELS:
        time.sleep(1) # using wait() here breaks it
        driver.find_element(By.ID, id).click()
        driver.find_element(By.ID, 'NextButton').click()

    time.sleep(5)

############# EXECUTION #############

if __name__ == '__main__':
    main()