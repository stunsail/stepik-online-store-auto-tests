from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong:first-of-type")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    
    
#Корзина .basket-mini.pull-right.hidden-xs
#Название продукта .product_main h1
#Сообщение о названии .alertinner strong:first-of-type
#Сообщение о цене .alertinner strong:last-of-type

    
