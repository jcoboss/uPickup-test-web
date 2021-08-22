from time import sleep

from selenium import webdriver
import unittest
import HtmlTestRunner


class createPlate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
        cls.driver.implicitly_wait(10)



    def test_a_open_menu(self):
        driver = self.driver

        driver.get('http://localhost:3000/')
        driver.implicitly_wait(5)

        menu_btn = driver.find_element_by_xpath(
            "//a[@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button']")
        menu_btn.click()
        sleep(5)
        self.assertEqual(driver.current_url, 'http://localhost:3000/menu')

    def test_b_click_new_plate(self):
        driver = self.driver

        driver.get('http://localhost:3000/menu')
        driver.implicitly_wait(5)

        new_btn = driver.find_element_by_id('add-new-plate')
        new_btn.click()
        sleep(5)
        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')


    def test_c_fill_new_plate_name(self):
        driver = self.driver

        driver.get('http://localhost:3000/new-plate')
        driver.implicitly_wait(5)

        name = driver.find_element_by_id('name')
        name.send_keys('Encebollado')
        sleep(5)

        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')

    def test_d_fill_new_plate_price(self):
        driver = self.driver

        driver.get('http://localhost:3000/new-plate')
        driver.implicitly_wait(5)

        price = driver.find_element_by_id('price')
        price.send_keys('3.00')
        sleep(5)

        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')


    def test_e_fill_new_plate_category(self):
        driver = self.driver

        driver.get('http://localhost:3000/new-plate')
        driver.implicitly_wait(5)

        category_select = driver.find_element_by_id('mui-component-select-category')
        category_select.click()
        sleep(5)

        breakfast = driver.find_element_by_xpath("//li[text()='Breakfast']").click()
        sleep(5)

        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')

    def test_f_fill_new_plate_picture(self):
        driver = self.driver

        price = driver.find_element_by_xpath("//input[@type='file']")
        price.send_keys('C:\\Users\\paula\\Documents\\Espolita\\8\\Software\\uPickup-test-web\\encebollado.jpg')
        sleep(5)

        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')

    def test_g_fill_new_plate_description(self):
        driver = self.driver

        driver.get('http://localhost:3000/new-plate')
        driver.implicitly_wait(5)

        price = driver.find_element_by_id('description')
        price.send_keys('Encebollado tipico ecuatoriano')
        sleep(5)

        self.assertEqual(driver.current_url, 'http://localhost:3000/new-plate')


    def test_h_add_new_plate(self):
        driver = self.driver

        driver.get('http://localhost:3000/new-plate')

        name = driver.find_element_by_id('name')
        name.send_keys('Encebollado')

        price = driver.find_element_by_id('price')
        price.send_keys('3.00')

        price = driver.find_element_by_id('description')
        price.send_keys('Encebollado tipico ecuatoriano')

        category_select = driver.find_element_by_id('mui-component-select-category')
        category_select.click()

        breakfast = driver.find_element_by_xpath("//li[text()='Breakfast']").click()


        price = driver.find_element_by_xpath("//input[@type='file']")
        price.send_keys('C:\\Users\\paula\\Documents\\Espolita\\8\\Software\\uPickup-test-web\\encebollado.jpg')

        sleep(5)

        new_btn = driver.find_element_by_id('add-new-plate')
        new_btn.click()

        sleep(5)

        self.assertNotEqual(driver.current_url, 'http://localhost:3000/new-plate')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/Acceptance testing'))
