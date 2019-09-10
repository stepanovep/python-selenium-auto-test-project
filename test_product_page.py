from pages.product_page import ProductPage

URL = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, URL)
    product_page.open()

    title = product_page.get_product_title()
    price = product_page.get_product_price()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.result_message_should_contain_title(title)
    product_page.basket_total_price_should_equal_product_price(price)
