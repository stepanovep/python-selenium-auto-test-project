from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_item_in_basket(self):
        items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        assert len(items) == 0, f'basket should be empty, but found {len(items)} items'

    def should_be_text_about_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert text == 'Your basket is empty. Continue shopping', f'should be text about basket is empty, but found: {text}'
