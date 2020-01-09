from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url

    def should_be_basket_url(self):
        assert self.browser.current_url.find("basket") !=-1, "Basket url is incorrect"
   
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty"
    
    def should_be_products_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Should be product in the basket"

    def should_be_a_message_about_empty_basket(self):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPRY_MESSAGE).text
        assert "Your basket is empty" in basket_empty_message, "Should be a message about empty basket"
