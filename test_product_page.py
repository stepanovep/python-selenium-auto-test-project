import random
import string
import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def generate_email():
    return str(time.time()) + '@fakemail.org'


def generate_password(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
REGISTRATION_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        login_page = LoginPage(browser, REGISTRATION_LINK)
        login_page.open()

        email = generate_email()
        password = generate_password()

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        product_page = ProductPage(self.browser, PRODUCT_PAGE_LINK)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        product_page = ProductPage(self.browser, PRODUCT_PAGE_LINK)
        product_page.open()

        title = product_page.get_product_title()
        price = product_page.get_product_price()

        product_page.add_product_to_basket()

        product_page.result_message_should_contain_title(title)
        product_page.basket_total_price_should_equal_product_price(price)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
    product_page.open()

    title = product_page.get_product_title()
    price = product_page.get_product_price()

    product_page.add_product_to_basket()

    product_page.result_message_should_contain_title(title)
    product_page.basket_total_price_should_equal_product_price(price)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
    product_page.open()

    basket_link = product_page.get_basket_link()
    basket_page = BasketPage(browser, basket_link)
    basket_page.open()

    basket_page.should_be_no_item_in_basket()
    basket_page.should_be_text_about_empty_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.should_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()
