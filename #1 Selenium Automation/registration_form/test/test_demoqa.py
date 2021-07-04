import unittest
from selenium import webdriver
from base.page_base import BaseClass
from page.demoqa_register_page import DemoQARegistrationForm


class DemoQA(unittest.TestCase):
    """ Test case is:

      1. Go to given website
      2. Hide ad if it exists
      3. Fill the desired areas
      4. Click submit button, then see results

      """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Packs\chromedriver.exe")
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.demoqa_registration = DemoQARegistrationForm(self.driver, self.methods)

    def test_demoQA(self):
        self.demoqa_registration.navigate_to_registration_page()
        self.demoqa_registration.hide_ad()
        self.demoqa_registration.fill_the_name_and_surname()
        self.demoqa_registration.fill_the_email()
        self.demoqa_registration.pick_gender()
        self.demoqa_registration.fill_the_phone(10)
        self.demoqa_registration.pick_date_of_birth()
        self.demoqa_registration.pick_hobbies()
        self.demoqa_registration.fill_the_address(50)
        self.demoqa_registration.submit()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
