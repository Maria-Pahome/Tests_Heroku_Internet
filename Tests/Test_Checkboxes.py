import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Checkboxes(unittest.TestCase):
    MAIN_PAGE = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    CHECKBOX1 = (By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
    CHECKBOX2 = (By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.implicitly_wait(6)
        self.driver.find_element(*self.MAIN_PAGE).click()
        self.driver.maximize_window()

    def test_click_on_checkboxes(self):
        self.driver.find_element(*self.CHECKBOX1).click()
        self.driver.find_element(*self.CHECKBOX2).click()
        self.driver.find_element(*self.CHECKBOX2).click()
        self.driver.find_element(*self.CHECKBOX1).click()

    def tearDown(self):
        self.driver.quit()
