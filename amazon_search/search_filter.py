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

    def apply_todays_deals_filter(self):
        todays_deals_element = self.driver.find_element(
            By.ID,
            'p_n_deal_type/26901098031'
        ).find_element(
            By.CSS_SELECTOR,
            'a[data-routing]'
        )
        todays_deals_element.click()

    def apply_discounted_products_filter(self):
        all_discounts_element = self.driver.find_element(
            By.ID,
            'p_n_deal_type/26901100031'
        )

        if all_discounts_element is None:
            print("The all discounts filter isn't available.")
            return

        all_discounts_link = all_discounts_element.find_element(
            By.CSS_SELECTOR,
            'a[data-routing]'
        )

        all_discounts_link.click()

    def filter_by_min_max_price(self, min_price, max_price):

        min_price_element = self.driver.find_element(By.ID, "low-price")
        max_price_element = self.driver.find_element(By.ID, "high-price")
        go_button = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='a-autoid-1-announce']")

        min_price_element.send_keys(min_price)
        max_price_element.send_keys(max_price)
        go_button.click()
