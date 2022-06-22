import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DragDrop(unittest.TestCase):
    DRAG_DROP_PG = (By.XPATH, '//a[contains(text(),"Drag")]')
    FIRST = (By.XPATH, '//div[@id="column-a"]')
    SECOND = (By.XPATH, '//div[@id="column-b"]')

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(*self.DRAG_DROP_PG).click()

    def tearDown(self):
        self.driver.quit()

    def test_dragA_drop_onB(self):
        f = self.driver.find_element(*self.FIRST)
        s = self.driver.find_element(*self.SECOND)
        actions = ActionChains(self.driver)
        actions.click_and_hold(f).move_by_offset(150, 100).pause(2).move_by_offset(-10, -10).release().perform()
        self.assertIn('A', s.text, 'Action not performed')
