import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Disappearing import Disappearing
from PageObjectModel.Pages.Home import Home

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(4)
home = Home(driver)
disappeared = Disappearing(driver)
home.click_on_disappear()
time.sleep(2)
disappeared.about_btn()
time.sleep(2)
driver.quit()



