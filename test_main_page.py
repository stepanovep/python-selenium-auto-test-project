import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'
PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()

    basket_link = page.get_basket_link()
    basket_page = BasketPage(browser, basket_link)
    basket_page.open()

    basket_page.should_be_no_item_in_basket()
    basket_page.should_be_text_about_empty_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
    product_page.open()

    basket_link = product_page.get_basket_link()
    basket_page = BasketPage(browser, basket_link)
    basket_page.open()

    basket_page.should_be_no_item_in_basket()
    basket_page.should_be_text_about_empty_basket()
