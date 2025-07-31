from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class HomePage(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.COMPANY_MENU = (By.LINK_TEXT, "Company")
        self.CAREERS = (By.LINK_TEXT, "Careers")
        self.NAVIGATION_BAR = (By.TAG_NAME, "nav")
        self.PAGE_TITLE = (By.TAG_NAME, "title")
        
    def open_homepage(self):
        """Opens Insider Home Page"""
        self.driver.maximize_window()
        self.driver.get("https://useinsider.com/")
        self.wait.until(EC.presence_of_element_located(self.NAVIGATION_BAR))
        
    def verify_homepage_opened(self):
        """Verifies Insider Home Page is opened"""
        try:
            # URL'yi kontrol et
            current_url = self.driver.current_url
            expected_url = "https://useinsider.com"
            
            self.assertIn(expected_url, current_url, f"Beklenen URL: {expected_url}, Mevcut URL: {current_url}")        
            return True
        except Exception as e:
            print(f"Ana sayfa doğrulama hatası: {e}")
            return False
            
    def click_company_menu(self):
        """Clicks on Company Menu"""
        company_menu = self.driver.find_element(*self.COMPANY_MENU)
        hover = ActionChains(self.driver).move_to_element(company_menu)
        hover.perform()
        
    def click_careers(self):
        """Clicks on Careers Link"""
        careers = self.driver.find_element(*self.CAREERS)
        careers.click()
        
    def navigate_to_careers(self):
        """Navigates to Careers Page from Company Menu"""
        self.click_company_menu()
        self.click_careers() 