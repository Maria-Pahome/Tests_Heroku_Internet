import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage(unittest.TestCase):
    USER = (By.ID, "username")
    PASS = (By.ID, "password")
    SUBMIT = (By.CLASS_NAME, "radius")
    ERROR = (By.ID, "flash-messages")
    LOGOUT = (By.CSS_SELECTOR, "#content > div > a")
    USERNAME = (By.CSS_SELECTOR, "#content > div > h4 > em:nth-child(1)")
    PASSWORD = (By.CSS_SELECTOR, "#content > div > h4 > em:nth-child(2)")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_correct_creds(self):
        self.driver.find_element(*self.USER).send_keys("tomsmith")
        self.driver.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.driver.find_element(*self.SUBMIT).click()
        flash_message = self.driver.find_element(*self.ERROR).text  # error text in page
        if "logged into" in flash_message:
            print("Test passed!")
            self.driver.find_element(*self.LOGOUT).click()
            time.sleep(2)
        else:
            print("Test failed!")




