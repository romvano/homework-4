# -*- coding: utf-8 -*-

from utils import Page, Component

class EventListPage(Page):
    PATH = '/blog/view/33/'

    @property
    def event(self):
        return Event(self.driver)

class Event(Component):
    HEADER_PATH = '//h1[@class="topic-title"]/a'
    SUBHEADER_PATH = '//a[@class="topic-blog"]'
    SUBMIT_BUTTON_PATH = '//button[@class="button"]'

    def open_event(self):
        self._wait_for_xpath(self.HEADER_PATH)
        self.driver.find_element_by_xpath(self.HEADER_PATH).click()

    def open_blog(self):
        self._wait_for_xpath(self.SUBHEADER_PATH)
        self.driver.find_element_by_xpath(self.SUBHEADER_PATH).click()

    def participate(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).click()

    def get_button_text(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).text

    def get_button_color(self):
        self._wait_for_xpath(self.SUBMIT_BUTTON_PATH)
        return self.driver.find_element_by_xpath(self.SUBMIT_BUTTON_PATH).value_of_css_property('background-color')