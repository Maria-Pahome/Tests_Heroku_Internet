import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)
driver.maximize_window()

BOX = (By.ID, "hot-spot")

action = ActionChains(driver)
action.context_click(driver.find_element(*BOX)).perform()

time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

driver.quit()

print("I am spaghetti code!")