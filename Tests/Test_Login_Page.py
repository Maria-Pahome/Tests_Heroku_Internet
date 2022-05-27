import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(2)

USER = (By.ID, "username")
PASS = (By.ID, "password")
SUBMIT = (By.CLASS_NAME, "radius")
ERROR = (By.ID, "flash-messages")
LOGOUT = (By.CSS_SELECTOR, "#content > div > a")

driver.find_element(*USER).send_keys("tomsmith")
time.sleep(2)
driver.find_element(*PASS).send_keys("SuperSecretPassword!")
time.sleep(2)
driver.find_element(*SUBMIT).click()
time.sleep(2)

flash_message = driver.find_element(*ERROR).text  # error text in page
if "logged into" in flash_message:
    print("Test passed!")
    driver.find_element(*LOGOUT).click()
    time.sleep(2)
else:
    print("Test failed!")

driver.quit()

print("I am spaghetti code!")