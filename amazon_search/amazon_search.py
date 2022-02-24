import os
from selenium import webdriver
from selenium.webdriver.common.by import By

import amazon_search.constants as const
from amazon_search.search_filter import SearchFilter


class AmazonSearch(webdriver.Chrome):

    def __init__(self, driver_path=const.DEFAULT_DRIVER_PATH,
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + self.driver_path

        super(AmazonSearch, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def open_amazon(self):
        self.get(const.AMAZON_URL)

    def accept_cookies(self):
        accept_cookies_button = self.find_element(By.NAME, 'accept')
        accept_cookies_button.click()

    def search_item(self, item):
        search_bar = self.find_element(By.ID, 'twotabsearchtextbox')
        search_bar.send_keys(item)

        search_button = self.find_element(By.ID, 'nav-search-submit-button')
        search_button.click()

    def apply_filter(self, desired_filter=0):

        search_filter = SearchFilter(driver=self)

        if desired_filter == 0:
            return
        elif desired_filter == 1:
            search_filter.filter_by_customer_ratings()




