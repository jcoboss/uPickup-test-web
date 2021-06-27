import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

class MenuAssertions(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path= r'./chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://localhost:3000/menu")

	def test_change_state(self):
		driver = self.driver
		selects = driver.find_elements_by_xpath('//div[@id="outlined-select-status"]')
		originalState = []
		newState = []
		for select in selects:
			select.click()
			selected_option = driver.find_element_by_xpath('//ul[@class="MuiList-root MuiMenu-list MuiList-padding"]/li[@aria-selected]')
			selected_option_text = selected_option.text
			originalState.append(selected_option_text)
			new_option = driver.find_element_by_xpath('//ul[@class="MuiList-root MuiMenu-list MuiList-padding"]/li[not(@aria-selected)]')
			new_option_text = new_option.text
			new_option.click()
			newState.append(new_option_text)
			sleep(0.5)

		selects = driver.find_elements_by_xpath('//div[@id="outlined-select-status"]')
		for i in range(len(selects)):
			self.assertNotEqual(originalState[i], newState[i])
			

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
        output="reports/menu", report_name="simple_test", add_timestamp=False))
