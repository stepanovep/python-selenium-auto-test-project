from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    RESULT_MESSAGES_FORM = (By.ID, 'messages')
    RESULT_MESSAGE_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    RESULT_BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info > div > p:nth-child(1) > strong')
