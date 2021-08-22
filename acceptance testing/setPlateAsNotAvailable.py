from time import sleep

from selenium import webdriver
import unittest
import HtmlTestRunner


class setOrderAsReady(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.get('http://localhost:3000/menu')

    def test_selectBox(self):
        driver = self.driver

        driver.find_element_by_id("outlined-select-status").click()

    def test_set_NotAvailable(self):
        driver = self.driver

        sleep(5)

        # driver.find_element_by_id("outlined-select-status").click()
        # sleep(5)

        driver.find_element_by_xpath("//li[text()='Not available']")
        sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/Acceptance testing'))
