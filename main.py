import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3747415774&f_AL=true&f_E=2&geoId=103077496&keywords=python&location=Athens%2C%20Attiki%2C%20Greece&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(URL)

signup = driver.find_element(By.LINK_TEXT, "Sign in")
signup.click()
time.sleep(1)

user=driver.find_element(By.ID, "username")
user.send_keys(username)
code = driver.find_element(By.ID,"password")
code.send_keys(password)
signin = driver.find_element(By.CSS_SELECTOR,".login__form_action_container button")
signin.click()
time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, "a[data-control-id]")

chat = driver.find_element(By.ID,"ember41")
chat.click()
time.sleep(2)
for job in jobs:
    try:
        print(job.get_attribute("href"))
        print(job.text)
        job.click()
        time.sleep(2)
        button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        print(button)

        button.click()
        time.sleep(2)
    except selenium.common.exceptions.ElementNotInteractableException:
        print("that one wasnt happening")
        continue