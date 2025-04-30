from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, driver, locator=''):
        self.locator = locator
        self.driver = driver


    def click(self):
        """ Click the element"""
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)