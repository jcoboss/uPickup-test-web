from time import sleep

from selenium import webdriver
import unittest
import HtmlTestRunner


class setOrderAsReady(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.get('http://localhost:3000/')

    def test_a_type_time(self):
        driver = self.driver


        time = driver.find_element_by_id('time')
        time.send_keys('5')
        sleep(5)

    def test_b_click_settime(self):
        driver = self.driver

        driver.implicitly_wait(5)

        driver.find_element_by_class_name("MuiButton-containedPrimary").click()
        sleep(5)


    def test_c_click_setReady(self):
        driver=self.driver
        sleep(5)

        driver.find_element_by_class_name("MuiButton-containedPrimary").click()
        sleep(5)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/Acceptance testing'))
