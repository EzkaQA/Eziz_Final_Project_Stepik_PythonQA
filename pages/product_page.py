from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product_to_card(self):

        addToBasket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        addToBasket.click()
        #BasePage.solve_quiz_and_get_code(self)

    def product_name_matches_added_product(self):
        bookName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        addedProductName = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert bookName == addedProductName, f"Expected book name is - {bookName}, actual book name is - {addedProductName}"

    def product_price_matches_added_product(self):
        bookPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basketTotalAfterAddingProduct = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_AFTER_ADDING_PRODUCT).text
        assert bookPrice == basketTotalAfterAddingProduct, f"Expected basket total is - {bookPrice}, actual basket total is - {basketTotalAfterAddingProduct}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
