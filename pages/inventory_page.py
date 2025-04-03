from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    SHOPPING_CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

    def is_inventory_page_displayed(self):
        """Check if the inventory page is displayed by verifying an element on the page."""
        try:
            inventory_header = self.driver.find_element(By.CLASS_NAME, "title")
            return inventory_header.is_displayed()  # True if element is visible
        except:
            return False

    def click_add_backpack(self):
        """Click the 'Add to Cart' button for the backpack."""
        try:
            self.click(self.ADD_BACKPACK_BUTTON)
        except Exception as e:
            print(f"Error clicking add-to-cart button: {e}")
    
    def click_add_cart(self):
        self.click(self.SHOPPING_CART_BUTTON)