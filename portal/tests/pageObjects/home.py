from django.conf import settings
from selenium import webdriver

from base import BasePage

class HomePage(BasePage):
    def __init__(self, browser):
        super(HomePage, self).__init__(browser)

        # check we're on the home page, raises an exception if not
        self.browser.find_element_by_id('home_page')