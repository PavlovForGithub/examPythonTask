from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#messages>div.alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")
