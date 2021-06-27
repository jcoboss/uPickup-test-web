import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

from InputExamples import newPlateExamples

class NewPlateAssertions(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path= r'./chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://localhost:3000/new-plate")

	def test_create_new_plate(self):
		driver = self.driver
		self.fillNewPlateForm(newPlateExamples[0])
		self.assertNotEqual(driver.current_url, "http://localhost:3000/menu")
			
	def test_create_new_plate2(self):
		driver = self.driver
		self.fillNewPlateForm(newPlateExamples[1])
		self.assertNotEqual(driver.current_url, "http://localhost:3000/menu")
	
	def test_create_new_plate3(self):
		driver = self.driver
		self.fillNewPlateForm(newPlateExamples[2])
		self.assertNotEqual(driver.current_url, "http://localhost:3000/menu")

	def fillNewPlateForm(self, data):
		driver = self.driver
		nameField = driver.find_element_by_id('name')
		nameTarget = data['productName']
		nameField.send_keys(nameTarget)

		priceField = driver.find_element_by_id('price')
		priceTarget = data['price']
		priceField.send_keys(priceTarget)
		
		descriptionField = driver.find_element_by_id('description')
		descriptionTarget = data['description']
		descriptionField.send_keys(descriptionTarget)
	
		submitButton = driver.find_element_by_id("add-new-plate")
		submitButton.click()

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
        output="reports/newPlate", report_name="simple_test", add_timestamp=False))