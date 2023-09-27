from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(.,'forgotten my password')]")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[value='Add to basket']")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_TOTAL_AFTER_ADDING_PRODUCT = (By.CSS_SELECTOR, ".alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success:nth-child(1)")

class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT = (By.XPATH, "//p[contains(text(), 'is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")