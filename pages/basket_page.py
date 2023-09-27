from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_has_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket has item list, but should not have"

    def basket_is_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            "Basket is empty text is not present, but should be"

    def basket_has_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket has no item list, but should have"