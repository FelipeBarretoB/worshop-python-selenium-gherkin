from behave import when
from pages.information_page import InformationPage
from pages.overview_page import OverviewPage
from selenium.webdriver.common.by import By

@when('the user fills out information')
def step_when_user_fills_information(context):
    context.information_page.fill_information("John", "Doe", "12345")
    context.information_page.click_continue()
    context.overview_page = OverviewPage(context.driver)