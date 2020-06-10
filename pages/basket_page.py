from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_page(self):
        assert self.is_not_element_present(*BasketPageLocators.TITLES_OF_PRODUCTS), \
            "Products are on page, but should not be"

    def should_see_empty_message_in_basket(self):
        message_on_page = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE_ELEMENT).text
        empty_message = "Your basket is empty."
        assert empty_message in message_on_page, \
            f"Expected message in page contains '{empty_message}' but actual is'{message_on_page}'"
