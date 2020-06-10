import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_see_equals_price_in_message(self, product_price):
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_MESSAGE).text
        assert product_price == price_in_message, \
            f"Expected price in basket message is '{product_price}' but actual is'{price_in_message}'"

    def should_see_equals_name_in_message(self, product_name):
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_MESSAGE).text
        assert product_name == name_in_message, \
            f"Expected name in basket message is '{product_name}' but actual is'{name_in_message}'"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
