from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_title(self):
        title_element = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        assert title_element, 'product title is not presented'
        print(f'product_title={title_element.text}')
        return title_element.text

    def get_product_price(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price_element, 'product price is not presented'
        print(f'product_price={price_element.text}')
        return price_element.text

    def result_message_should_contain_title(self, product_title):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_FORM)
        title_in_result_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_TITLE).text
        print(f'message_result={title_in_result_message}')
        assert product_title == title_in_result_message, f'expected: {product_title}, got: {title_in_result_message}'

    def basket_total_price_should_equal_product_price(self, product_price):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_FORM)
        basket_total_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_TOTAL_PRICE).text
        print(f'basket_total_price={basket_total_price}')
        assert basket_total_price == product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_TITLE), 'Success message is presented, but should not be'

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_TITLE), 'Success message should disappeared, but it did not'
