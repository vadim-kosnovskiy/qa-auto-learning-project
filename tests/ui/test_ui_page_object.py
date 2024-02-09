from modules.ui.page_objects.home_page import HomePage
from modules.ui.page_objects.sign_in_page import SignInPage
import pytest
import time


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()


@pytest.mark.ui
def test_check_default_language():
    home_page = HomePage()
    home_page.go_to()
    time.sleep(3)
    language = home_page.select_language_ua()

    assert language == "УКР"

    home_page.close()


@pytest.mark.ui
def test_add_product_to_bottom_cart():
    product_name = "Samsung Galaxy Buds 2 Pro Gray"
    home_page = HomePage()
    home_page.go_to()
    time.sleep(10)
    found_name = home_page.add_product_to_bottom_cart(product_name)

    assert product_name in found_name

    home_page.close()
