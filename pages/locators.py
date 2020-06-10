from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "div.basket-mini span>a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#messages>div.alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages>div.alert-success")


class BasketPageLocators():
    EMPTY_MESSAGE_ELEMENT = (By.CSS_SELECTOR, "div#content_inner>p")
    TITLES_OF_PRODUCTS = (By.CSS_SELECTOR, "div.row h2")
