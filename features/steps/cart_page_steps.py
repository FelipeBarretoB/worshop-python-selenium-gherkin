from behave import when
from pages.cart_page import CartPage
from pages.information_page import InformationPage
from selenium.webdriver.common.by import By

@when('the user clicks on the checkout button')
def step_when_user_clicks_checkout(context):
    context.cart_page.click_checkout()
    context.information_page = InformationPage(context.driver)