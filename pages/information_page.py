from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InformationPage(BasePage):
    NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_information(self, first_name, last_name, zip_code):
        self.type(self.NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.ZIP_CODE_INPUT, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)