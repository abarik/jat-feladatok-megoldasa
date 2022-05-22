from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config import TestData_01

class Test01(object):
    def setup(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()
        self.browser.get(TestData_01.URL)

    def teardown(self):
        self.browser.quit()

    def test_first_testcase(self):
        assert True
