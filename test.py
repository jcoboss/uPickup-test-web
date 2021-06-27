import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class EcomerceHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver')
        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.maximize_window()
        #driver.implicitly_wait(10)
    
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")
        
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main(verbosity= 2)