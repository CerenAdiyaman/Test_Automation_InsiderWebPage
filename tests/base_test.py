import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io

class BaseTest:
    def setup_method(self):
        """Her test metodundan önce çalışır - WebDriver'ı başlatır"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-cookies')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--disable-features=VizDisplayCompositor')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        self.wait = WebDriverWait(self.driver, 10)
        
    def teardown_method(self):
        """Her test metodundan sonra çalışır - WebDriver'ı kapatır"""
        if hasattr(self, 'driver'):
            self.driver.quit()
    
    def take_screenshot(self, name="screenshot"):
        """Test başarısız olduğunda screenshot alır"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{name}_{timestamp}.png"
            
            # Screenshots klasörünü oluştur
            os.makedirs("screenshots", exist_ok=True)
            
            # Screenshot al
            screenshot = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(screenshot))
            image.save(filename)
            
            print(f"Screenshot kaydedildi: {filename}")
            return filename
        except Exception as e:
            print(f"Screenshot alma hatası: {e}")
            return None
    
    def wait_for_element(self, locator, timeout=10):
        """Element görünür olana kadar bekler"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_not_found")
            raise
    
    def wait_for_element_clickable(self, locator, timeout=10):
        """Element tıklanabilir olana kadar bekler"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.take_screenshot("element_not_clickable")
            raise
    
    def scroll_to_element(self, element):
        """Elemente scroll yapar"""
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(1)
            
        except Exception as e:
            print(f"Scroll hatası: {e}")
            # Son çare olarak sayfanın sonuna scroll
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
