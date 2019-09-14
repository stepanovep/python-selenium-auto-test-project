import random
import string
import time

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def generate_email():
    return str(time.time()) + '@fakemail.org'


def generate_password(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():

    product_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    registration_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        login_page = LoginPage(browser, self.registration_link)
        login_page.open()

        email = generate_email()
        password = generate_password()

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        product_page = ProductPage(self.browser, self.product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        product_page = ProductPage(self.browser, self.product_link)
        product_page.open()

        title = product_page.get_product_title()
        price = product_page.get_product_price()

        product_page.add_product_to_basket()

        product_page.result_message_should_contain_title(title)
        product_page.basket_total_price_should_equal_product_price(price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.should_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
