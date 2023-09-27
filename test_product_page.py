from .pages import product_page, basket_page
import pytest
from mimesis import Person
from mimesis.locales import Locale

from .pages.login_page import LoginPage

productPageLink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('promoOffers', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                        "?promo=offer5", "?promo=offer6",   pytest.param("?promo=offer7",marks=pytest.mark.xfail),
                                         "?promo=offer8",  "?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promoOffers):
    link = f"{productPageLink}{promoOffers}"
    page = product_page.ProductPage(browser, link)  # check the basket total, save the price in variable basketTotal
    page.open()  # check the books price and save to the variable bookPrice
    page.should_add_product_to_card()  # check the books name and save it to the variable bookName
    page.product_name_matches_added_product()  # assert that book is added to the basket(names are matching)
    page.product_price_matches_added_product()  # assert that basket price changed according to added book price


@pytest.mark.xfail(reason="should fail for now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.should_add_product_to_card()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="should fail for now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.should_add_product_to_card()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = product_page.ProductPage(browser, productPageLink)
    page.open()
    page.go_to_basket()
    basketPage = basket_page.BasketPage(browser, browser.current_url)
    basketPage.basket_has_no_items()
    basketPage.basket_is_empty_message_present()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = Person(locale=Locale.EN).email()
        user_password = Person(locale=Locale.EN).password(length=20)
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, user_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = product_page.ProductPage(browser, productPageLink)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"{productPageLink}?promo=offer0"
        page = product_page.ProductPage(browser, link)  # check the basket total, save the price in variable basketTotal
        page.open()  # check the books price and save to the variable bookPrice
        page.should_add_product_to_card()  # check the books name and save it to the variable bookName
        page.product_name_matches_added_product()  # assert that book is added to the basket(names are matching)
        page.product_price_matches_added_product()  # assert that basket price changed according to added book price
