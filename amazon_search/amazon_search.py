import os
from selenium import webdriver

import amazon_search.constants as const


class AmazonSearch(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\Users\prith\Desktop\Side-Learning\Python Projects\chromedriver_win32",
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

