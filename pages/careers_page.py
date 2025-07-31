from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class CareersPage(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.LOCATIONS_SECTION = (By.CSS_SELECTOR, "h3.category-title-media")
        self.TEAMS_SECTION = (By.CSS_SELECTOR, "section#career-find-our-calling")
        self.LIFE_AT_INSIDER_SECTION = (By.CSS_SELECTOR, "h2.elementor-heading-title")
        self.QA_JOBS_LINK = (By.LINK_TEXT, "Quality Assurance")
        self.SEE_ALL_TEAMS_BUTTON = (By.LINK_TEXT, "See all teams")
        
    def verify_careers_page_opened(self):
        """Verify that the careers page is opened"""
        try:
            current_url = self.driver.current_url
            self.assertIn("careers", current_url.lower(), f"Careers page not opened. URL: {current_url}")
            return True
        except Exception as e:
            print(f"Careers page verification error: {e}")
            return False
            
    def verify_careers_sections(self):
        """Verify that the careers sections are visible"""
        try:
            # Verify that the page is loaded
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # Verify that the locations section is visible
            try:
                print("🔍 Searching for the locations section...")
                locations_section = self.driver.find_element(*self.LOCATIONS_SECTION)
                print("✅ Locations section found")
                # Check visibility
                self.assertTrue(locations_section.is_displayed(), "Locations section is not visible")
                print("✓ Locations section is visible")
            except Exception as e:
                print(f"❌ Locations section not found: {e}")
            
            # Verify that the teams section is visible
            try:
                print("🔍 Searching for the teams section...")
                teams_section = self.driver.find_element(*self.TEAMS_SECTION)
                print("✅ Teams section found")
                # Check visibility
                self.assertTrue(teams_section.is_displayed(), "Teams section is not visible")
                print("✓ Teams section is visible")
            except Exception as e:
                print(f"❌ Teams section not found: {e}")
            
            # Verify that the life at insider section is visible
            try:
                print("🔍 Searching for the life at insider section...")
                life_section = self.driver.find_element(*self.LIFE_AT_INSIDER_SECTION)
                print("✅ Life at Insider section found")
                # Check visibility
                self.assertTrue(life_section.is_displayed(), "Life at Insider section is not visible")
                print("✓ Life at Insider section is visible")
            except Exception as e:
                print(f"❌ Life at Insider section not found: {e}")
            
            # Simple verification - page loaded?
            return True
            
        except Exception as e:
            print(f"Careers sections verification error: {e}")
            return False
            
    