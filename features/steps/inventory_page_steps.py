from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

@when('the user adds a backpack to the cart')
def step_when_user_logs_in_valid(context):
    context.inventory_page.click_add_backpack()

@when('the user clicks on the shopping cart icon')
def step_when_user_logs_in_valid(context):
    context.inventory_page.click_add_cart()
    context.cart_page = CartPage(context.driver)
