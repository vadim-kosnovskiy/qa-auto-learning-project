from selenium.webdriver import ActionChains

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    URL = "https://comfy.ua/ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(HomePage.URL)

    def select_language_ua(self):
        language = self.driver.find_element(By.CLASS_NAME, "lang-sw__lang-link_current").text

        return language

    def add_product_to_bottom_cart(self, product_name: str):
        headphones = self.driver.find_element(By.CSS_SELECTOR, "a[href*='https://comfy.ua/ua/audio/']")
        samsung = self.driver.find_element(By.CSS_SELECTOR, "a[href*='https://comfy.ua/ua/nayshniki/brand__samsung/']")

        actions = ActionChains(self.driver)
        actions.move_to_element(headphones).move_by_offset(-8, 2)
        actions.move_to_element(samsung).move_by_offset(5, -1)
        actions.click().perform()
        self.driver.implicitly_wait(5)

        hf = self.driver.find_element(By.ID, "pr - 2119285")
        buy_button = hf.find_element(By.CSS_SELECTOR, "div.products-list-control")
        buy_button.click()
        # escape pop-up window
        ActionChains(self.driver).click(Keys.ESCAPE)

        bottom_cart = self.driver.find_element(By.CLASS_NAME, "header-bottom-cart header-bottom-controls__item")
        bottom_cart.click()
        find_product_name = self.driver.find_element(By.PARTIAL_LINK_TEXT, product_name).text

        return find_product_name
