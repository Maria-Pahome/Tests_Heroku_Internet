import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class DisappearingElement(unittest.TestCase):
    ORIGINAL_PAGE = (By.XPATH, '//*[@id="content"]/ul/li[9]/a')
    HOME_BTN = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')
    ABOUT_BTN = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
    ERROR = (By.XPATH, '/html/body/h1')
    CONTACT_US_BTN = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/a')
    PORTFOLIO_BTN = (By.XPATH, '//*[@id="content"]/div/ul/li[4]/a')
    GALLERY_BTN = (By.XPATH, '//*[@id="content"]/div/ul/li[5]/a')
    MAIN_CONTAINER = (By.XPATH, '//*[@id="content"]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(*self.ORIGINAL_PAGE).click()

    def tearDown(self):
        self.driver.quit()

    def test_click_on_home_btn(self):
        self.driver.find_element(*self.HOME_BTN).click()
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEquals(expected, actual, "Failed! This is not home page!")

    def test_click_on_about_btn(self):
        self.driver.find_element(*self.ABOUT_BTN).click()
        error_msg = self.driver.find_element(*self.ERROR)
        self.assertIn(error_msg.text, 'Not Found', 'Not the correct error have been found!')

    def test_click_on_contact_us(self):
        self.driver.find_element(*self.CONTACT_US_BTN).click()
        error_msg2 = self.driver.find_element(*self.ERROR)
        self.assertIn(error_msg2.text, 'Not found', 'Not the correct error has been found!')

    def test_click_on_portfolio_btn(self):
        self.driver.find_element(*self.PORTFOLIO_BTN).click()
        error_msg3 = self.driver.find_element(*self.ERROR)
        self.assertIn(error_msg3.text, 'Custom error', 'Not the correct error has been found!')

    def test_find_missing_page(self):
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div > ul > li:nth-child(5)')))
        finally:
            self.driver.quit()
