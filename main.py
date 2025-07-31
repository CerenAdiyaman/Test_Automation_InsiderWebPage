#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insider Test Automation Project
Test Automation for Insider Careers Page
"""

import sys
import os
import pytest
from datetime import datetime

# Proje kök dizinini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_tests():
    """Testleri çalıştırır"""
    print("🚀 Insider Test Automation Project başlatılıyor...")
    print("=" * 60)
    
    # Test sonuçları için klasör oluştur
    os.makedirs("test_results", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    
    # Test çalıştırma zamanı
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Pytest komutları
    pytest_args = [
        "tests/",
        "-v",  # Verbose output
        "--tb=short",  # Kısa traceback
        "--capture=no",  # Print çıktılarını göster
    ]
    
    try:
        # Testleri çalıştır
        exit_code = pytest.main(pytest_args)
        
        if exit_code == 0:
            print("\n✅ Tüm testler başarıyla tamamlandı!")
        else:
            print(f"\n❌ Bazı testler başarısız oldu. Exit code: {exit_code}")
            
        return exit_code
        
    except Exception as e:
        print(f"❌ Test çalıştırma hatası: {e}")
        return 1

def run_specific_test(test_name):
    """Belirli bir testi çalıştırır"""
    print(f"🎯 Belirli test çalıştırılıyor: {test_name}")
    print("=" * 60)
    
    pytest_args = [
        f"tests/test_insider_careers.py::TestInsiderCareers::{test_name}",
        "-v",
        "--tb=short",
        "--capture=no",
    ]
    
    try:
        exit_code = pytest.main(pytest_args)
        return exit_code
    except Exception as e:
        print(f"❌ Test çalıştırma hatası: {e}")
        return 1

def show_available_tests():
    """Mevcut testleri listeler"""
    print("📋 Mevcut Testler:")
    print("=" * 30)
    print("1. test_01_homepage_navigation")
    print("2. test_02_careers_page_navigation")
    print("3. test_03_qa_jobs_filtering")
    print("4. test_04_job_details_verification")
    print("5. test_05_view_role_redirect")
    print("6. test_complete_insider_careers_flow")
    print("\nTüm testleri çalıştırmak için: python main.py")
    print("Belirli test çalıştırmak için: python main.py <test_name>")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        if test_name == "--help" or test_name == "-h":
            show_available_tests()
        else:
            run_specific_test(test_name)
    else:
        run_tests()
