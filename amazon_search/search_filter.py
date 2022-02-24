from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SearchFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filter_by_customer_ratings(self):
        four_star_filter = self.driver.find_element(By.CSS_SELECTOR, 'section[aria-label="4 Stars & Up"]')
        four_star_filter.click()