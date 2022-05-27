import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
time.sleep(2)

IMG = (By.CSS_SELECTOR, "#content > div > img:nth-child(4)")

displayed_img = driver.find_element(*IMG).is_displayed()
time.sleep(3)
if displayed_img is True:
    print("This img is not broken")

driver.quit()
