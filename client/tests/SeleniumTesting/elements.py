

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import PageLocators

class Email_Field_Elements(object):
    """ This class is to initiate set and get attributes for all page elements """

    def __set__(self, instance, value):
        """ This sets the value of the HTML element """
        driver = instance.driver
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*self.forEdit))
        element = driver.find_element(*self.forEdit)
        element.clear()
        element.send_keys(value)

    def __get__(self, instance, owner):
        """ Gets the text value of the HTML element """
        driver = instance.driver
        # Waiting for the element to be visible
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*self.forRead))
        # Extracting element value
        element = driver.find_element(*self.forRead)
        return element.text

class Password_Field_Elements(object):
    """ This class is to initiate set and get attributes for all page elements """

    def __set__(self, instance, value):
        """ This sets the value of the HTML element """
        driver = instance.driver
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*self.forEdit))
        element = driver.find_element(*self.forEdit)
        element.clear()
        element.send_keys(value)

    def __get__(self, instance, owner):
        """ Gets the text value of the HTML element """
        driver = instance.driver
        # Waiting for the element to be visible
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*self.forRead))
        # Extracting element value
        element = driver.find_element(*self.forRead)
        return element.text