from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CompletePage(BasePage):
    TITLE_HEADER = (By.CLASS_NAME, "complete-header")

    def is_complete_displayed(self):
        inventory_header = self.driver.find_element(By.CLASS_NAME, "complete-header")
        return inventory_header.is_displayed()  # True if element is visible