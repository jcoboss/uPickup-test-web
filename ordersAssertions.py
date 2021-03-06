import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from HtmlTestRunner import HTMLTestRunner

class OrderAssertions(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path= r'./chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://localhost:3000/")

	def test_order_list(self):
	    self.assertGreaterEqual(len(self.driver.find_elements_by_xpath("//div[contains(@id, 'order')]")), 1)

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def	is_element_present(self, how, what):
		try:  #busca los elementos según el parámetro
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner=HTMLTestRunner(
        output="reports/orders", report_name="simple_test", add_timestamp=False))