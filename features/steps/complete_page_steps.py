from behave import then
from pages.complete_page import CompletePage
from selenium.webdriver.common.by import By

@then('the user should see a confirmation message')
def step_then_user_sees_confirmation(context):
    assert context.complete_page.is_complete_displayed(), "Confirmation message is not displayed"
