from .pages.product_page import ProductPage
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"#open the page
    page = ProductPage(browser, link)#check the basket total, save the price in variable basketTotal
    page.open()#check the books price and save to the variable bookPrice
    page.should_add_product_to_card()#check the books name and save it to the variable bookName
    page.product_name_matches_added_product()#assert that book is added to the basket(names are matching)
    page.product_price_matches_added_product()#assert that basket price changed according to added book price

