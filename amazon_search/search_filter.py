from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SearchFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_customer_ratings_filter(self, customer_rating):

        element_label = str(customer_rating) + " Stars & Up"

        if customer_rating == 1:
            element_label = element_label.replace("Stars", "Star")

        print(element_label)

        star_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'section[aria-label="{element_label}"]'
        )
        star_filter.click()
