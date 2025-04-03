from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OverviewPage(BasePage):
    FINNISH_BUTTON = (By.ID, "finish")

    def click_finish(self):
        self.click(self.FINNISH_BUTTON)