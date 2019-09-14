from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL_BOX = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_BOX = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM_BOX = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE_FORM = (By.ID, 'messages')
    SUCCESS_MESSAGE_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    SUCCESS_MESSAGE_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info > div > p:nth-child(1) > strong')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
