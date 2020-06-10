import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='okay_link')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_see_equals_price_in_message(page.get_product_price())
    page.should_see_equals_name_in_message(page.get_product_name())
