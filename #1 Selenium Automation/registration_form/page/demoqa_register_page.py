from selenium.webdriver.common.by import By


class DemoQARegistrationForm:
    """Website register page class to user registration"""

    website = 'https://demoqa.com/automation-practice-form'
    email = 'test@test.com'
    FORM_ASSERTION = (By.ID, 'userForm')
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.ID, 'userEmail')
    GENDER = (By.ID, 'gender-radio-1')
    PHONE_NUMBER = (By.ID, 'userNumber')
    DATE_OF_BIRTH = (By.ID, 'dateOfBirthInput')
    MONTH_DROPDOWN = (By.CLASS_NAME, 'react-datepicker__month-select')
    YEAR_DROPDOWN = (By.CLASS_NAME, 'react-datepicker__year-select')
    DATE_PICKER_MONTH = (By.CSS_SELECTOR, '[value="5"]')
    DATE_PICKER_YEAR = (By.CSS_SELECTOR, '[value="2005"]')
    DATE_PICKER_DAY = (By.CLASS_NAME, 'react-datepicker__day')
    SUBJECTS = (By.CLASS_NAME, 'subjects-auto-complete__control')
    HOBBIES = (By.ID, 'hobbies-checkbox-1')
    UPLOAD_PICTURE = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
    SUBMIT_BTN = (By.ID, 'submit')
    CLOSE_BTN = (By.ID, 'closeLargeModal')
    HIDE_AD = (By.ID, 'close-fixedban')

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def navigate_to_registration_page(self):
        """
        Navigates to registration page

        """
        self.driver.get(self.website)
        assert self.methods.element_exists(self.FORM_ASSERTION), "Register Page could not loaded!"

    def hide_ad(self):
        """
        Hides ad if it exists to prevent any ElementClickInterceptedException

        """
        if self.methods.element_exists(self.HIDE_AD):
            self.methods.wait_for_element(self.HIDE_AD).click()

    def fill_the_name_and_surname(self):
        """
        Fills name and surname tex boxes with random string generator

        """
        random_name = self.methods.create_random_string(5)
        random_surname = self.methods.create_random_string(10)
        self.methods.wait_for_element(self.FIRST_NAME).send_keys(random_name)
        self.methods.wait_for_element(self.LAST_NAME).send_keys(random_surname)

    def fill_the_email(self):
        """
        Fills email area with defined parameter

        """
        self.methods.wait_for_element(self.EMAIL).send_keys(self.email)

    def pick_gender(self):
        """
        Picks gender in radiobutton section. Used execute_script to run this step

        """
        radio = self.methods.presence_of_element_located(self.GENDER)
        self.driver.execute_script("arguments[0].click();", radio)

    def fill_the_phone(self, size):
        """
        Fills phone number section with random digit generator

        """
        random_number = self.methods.create_random_digit(size)
        self.methods.wait_for_element(self.PHONE_NUMBER).send_keys(random_number)

    def pick_date_of_birth(self):
        """
        Selects a date in date picker. It might be used random date selection
        in this method, like random phone and name usages.
        However I didn't use it, due to date picker complexity

        """
        self.methods.wait_for_element(self.DATE_OF_BIRTH).click()
        self.methods.wait_for_element(self.YEAR_DROPDOWN).click()
        self.methods.wait_for_element(self.DATE_PICKER_YEAR).click()
        self.methods.wait_for_element(self.MONTH_DROPDOWN).click()
        self.methods.wait_for_element(self.DATE_PICKER_MONTH).click()
        self.methods.wait_for_element(self.DATE_PICKER_DAY).click()

    def pick_hobbies(self):
        """
        Picks a hobby on checkboxes section

        """
        checkbox = self.methods.presence_of_element_located(self.HOBBIES)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def fill_the_address(self, size):
        """
        Fills the address area with a random string
        :param size: Defines the size of the address string

        """
        random_string = self.methods.create_random_string(size)
        self.methods.wait_for_element(self.CURRENT_ADDRESS).send_keys(random_string)

    def submit(self):
        """
        Submits the form then assert it

        """
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.methods.element_hover(self.SUBMIT_BTN)
        self.methods.wait_for_element(self.SUBMIT_BTN).click()
        assert self.methods.element_exists(self.CLOSE_BTN), "Form Could not been submitted"
