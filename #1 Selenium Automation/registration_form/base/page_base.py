import random
import string
from random import randint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: Locator of the element to find

        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    def element_exists(self, selector, multiple=False):
        """
        Return true if element/elements present and false if element/elements absent
        :param selector: Locator of the element to find
        :param multiple: False in default, if True returns the list of WebElements once they are located

        """
        if not multiple:
            try:
                self.wait.until(ec.presence_of_element_located(selector))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(ec.presence_of_all_elements_located(selector))
                return True
            except TimeoutException:
                return False

    def presence_of_all_elements_located(self, selector):
        """
        Waits until all elements are present on the DOM of a page and visible then returns list of elements
        :param selector: Locator of the desired elements

        """
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def presence_of_element_located(self, selector):
        """
        Waits until a element i present on the DOM of a page and visible then returns element
        :param selector: Locator of the desired element

        """
        return self.wait.until(ec.presence_of_element_located(selector))

    @staticmethod
    def create_random_number(first_value, second_value):
        """
        Return random number between parameters
        :param first_value: beginning value of the range
        :param second_value: last value of the range

        """
        return randint(first_value, second_value)

    @staticmethod
    def create_random_string(size=1):
        """
        Create random string to use it in name generator
        :param int size: Size of desired random string
        :return: Random string
        :rtype: string

        """
        chars = string.ascii_uppercase
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def create_random_digit(size):
        """
        Create random integer to use it in name generator
        :return: Random integer with given parameter
        :rtype: int

        """
        chars = string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def element_hover(self, selector):
        """
        Hover over the selected element
        :param selector: Locator of the element to find

        """
        hover_element = self.wait_for_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()
