import pytest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

class TestInsiderCareers(BaseTest):
    """Insider Careers test senaryoları"""
    
    def test_01_homepage_navigation(self):
        """Test Step 1: Ana sayfa açılması ve doğrulanması"""
        try:
            home_page = HomePage(self.driver)
            
            # Ana sayfayı aç
            home_page.open_homepage()
            
            # Ana sayfanın başarıyla açıldığını doğrula
            home_page.verify_homepage_opened()
            
            print("✓ Test Step 1 başarılı: Insider ana sayfası başarıyla açıldı")
            
        except Exception as e:
            self.take_screenshot("homepage_navigation_failed")
            raise e
    
    def test_02_careers_page_navigation(self):
        """Test Step 2: Company menüsünden Careers sayfasına gitme ve bölümleri doğrulama"""
        try:
            home_page = HomePage(self.driver)
            careers_page = CareersPage(self.driver)
            
            # Ana sayfayı aç
            home_page.open_homepage()
            
            # Company menüsünden Careers sayfasına git
            home_page.navigate_to_careers()
            
            # Careers sayfasının açıldığını doğrula
            careers_page.verify_careers_page_opened()
            
            # Careers sayfasındaki bölümleri doğrula
            careers_page.verify_careers_sections()
            
            print("✓ Test Step 2 başarılı: Careers sayfası açıldı ve bölümler doğrulandı")
            
        except Exception as e:
            self.take_screenshot("careers_navigation_failed")
            raise e
    
    def test_03_qa_jobs_filtering(self):
        """Test Step 3: QA Jobs sayfasına gitme ve filtreleme"""
        try:
            qa_jobs_page = QAJobsPage(self.driver)
            
            # QA Jobs sayfasını aç
            qa_jobs_page.open_qa_jobs_page()

            # "See all QA jobs" butonuna tıklama
            qa_jobs_page.click_see_all_qa_jobs()
            
            # Lokasyon filtresini ayarla
            qa_jobs_page.filter_by_location("Istanbul, Turkey")
            
            # Departman filtresini ayarla
            qa_jobs_page.filter_by_department("Quality Assurance")
            
            # Filtreleri uygula
            qa_jobs_page.apply_filters()
            
            # İş listelerinin görüntülendiğini doğrula
            qa_jobs_page.verify_job_listings_displayed()
            
            print("✓ Test Step 3 başarılı: QA Jobs filtrelendi ve listeler görüntülendi")
            
        except Exception as e:
            self.take_screenshot("qa_jobs_filtering_failed")
            raise e
    
    def test_04_job_details_verification(self):
        """Test Step 4: İş listelerinin detaylarını doğrulama"""
        try:
            qa_jobs_page = QAJobsPage(self.driver)
            
            # QA Jobs sayfasını aç ve filtrele
            qa_jobs_page.open_qa_jobs_page()
            qa_jobs_page.click_see_all_qa_jobs()
            
            # Filtreleri uygula
            qa_jobs_page.filter_by_location("Istanbul, Turkey")
            qa_jobs_page.filter_by_department("Quality Assurance")
            qa_jobs_page.apply_filters()
            
            # İş detaylarını doğrula
            qa_jobs_page.verify_job_details()
            
            print("✓ Test Step 4 başarılı: İş listesi detayları doğrulandı")
            
        except Exception as e:
            self.take_screenshot("job_details_verification_failed")
            raise e
    
    def test_05_view_role_redirect(self):
        """Test Step 5: View Role butonuna tıklama ve Lever formuna yönlendirme"""
        try:
            qa_jobs_page = QAJobsPage(self.driver)
            
            # QA Jobs sayfasını aç ve filtrele
            qa_jobs_page.open_qa_jobs_page()
            qa_jobs_page.filter_by_location("Istanbul, Turkey")
            qa_jobs_page.filter_by_department("Quality Assurance")
            qa_jobs_page.apply_filters()
            
            # İlk iş için View Role butonuna tıkla
            qa_jobs_page.click_view_role_button(0)
            
            # Lever başvuru formuna yönlendirmeyi doğrula
            qa_jobs_page.verify_application_form_redirect()
            
            print("✓ Test Step 5 başarılı: View Role butonu Lever formuna yönlendirdi")
            
        except Exception as e:
            self.take_screenshot("view_role_redirect_failed")
            raise e
    
    def test_complete_insider_careers_flow(self):
        """Tüm test senaryosunu tek seferde çalıştırır"""
        try:
            home_page = HomePage(self.driver)
            careers_page = CareersPage(self.driver)
            qa_jobs_page = QAJobsPage(self.driver)
            
            # Step 1: Ana sayfa açılması
            home_page.open_homepage()
            home_page.verify_homepage_opened()
            print("✓ Step 1: Ana sayfa başarıyla açıldı")
            
            # Step 2: Careers sayfasına gitme
            home_page.navigate_to_careers()
            careers_page.verify_careers_page_opened()
            careers_page.verify_careers_sections()
            print("✓ Step 2: Careers sayfası açıldı ve bölümler doğrulandı")
            
            # Step 3: QA Jobs sayfasına gitme ve filtreleme
            qa_jobs_page.open_qa_jobs_page()
            qa_jobs_page.click_see_all_qa_jobs()
            qa_jobs_page.filter_by_location("Istanbul, Turkey")
            qa_jobs_page.filter_by_department("Quality Assurance")
            qa_jobs_page.apply_filters()
            qa_jobs_page.verify_job_listings_displayed()
            print("✓ Step 3: QA Jobs filtrelendi ve listeler görüntülendi")
            
            # Step 4: İş detaylarını doğrulama
            qa_jobs_page.verify_job_details()
            print("✓ Step 4: İş listesi detayları doğrulandı")
            
            # Step 5: View Role butonuna tıklama
            qa_jobs_page.click_view_role_button(0)
            qa_jobs_page.verify_application_form_redirect()
            print("✓ Step 5: View Role butonu Lever formuna yönlendirdi")
            
            print("\n Tüm test senaryoları başarıyla tamamlandı!")
            
        except Exception as e:
            self.take_screenshot("complete_flow_failed")
            print(f" Test senaryosu başarısız: {e}")
            raise e 