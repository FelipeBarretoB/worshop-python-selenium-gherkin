from behave import when
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage
from selenium.webdriver.common.by import By

@when('the user clicks on the finish button')
def step_when_user_clicks_finish(context):
    context.overview_page.click_finish()
    context.complete_page = CompletePage(context.driver)
