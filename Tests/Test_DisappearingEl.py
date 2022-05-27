import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjectModel.Pages.Disappearing import Disappearing
from PageObjectModel.Pages.Home import Home


class DisappearingEl(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_home_btn_error(self):
        home = Home(self.driver)
        disappearing = Disappearing(self.driver)
        home.click_on_disappear()
        disappearing.home_btn()

    def tearDown(self) -> None:
        self.driver.quit()


print("This should be unittest")
