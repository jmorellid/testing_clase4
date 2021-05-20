from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage


class ContactPage(BasePage):
    URL = 'https://mrtesteloper.wordpress.com/contacto/'
    NAME_ID = (By.ID, 'g332-nombre')
    EMAIL_ID = (By.ID, 'g332-correoelectrnico')
    MSG_ID = (By.ID, 'contact-form-comment-g332-mensaje')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_name(self, name):
        self.driver.find_element(*self.NAME_ID).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_ID).send_keys(email)

    def set_message(self, message):
        self.driver.find_element(*self.MSG_ID).send_keys(message)

    def get_name(self):
        return self.driver.find_element(*self.NAME_ID).get_attribute("value")

    def get_email(self):
        return self.driver.find_element(*self.EMAIL_ID).get_attribute("value")

    def get_message(self):
        return self.driver.find_element(*self.MSG_ID).get_attribute("value")