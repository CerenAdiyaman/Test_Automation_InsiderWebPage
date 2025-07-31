# Insider Test Automation Project

This project contains test automation for Insider website's homepage, navigation, and QA job listings functionality. Tests are developed in Python using Selenium WebDriver following POM (Page Object Model) principles.

## Test Scenarios

### Test Steps:
1. **Homepage Opening**: Successfully opening https://useinsider.com/
2. **Navigation**: Going to Careers page from Company menu and verifying sections
3. **QA Jobs Filtering**: Filtering Quality Assurance jobs by location and department
4. **Job Details Verification**: Checking that each job listing contains correct information
5. **Application Form Redirect**: Verifying "View Role" button redirects to Lever application form

## Technologies

- **Programming Language**: Python 3.8+
- **Test Framework**: Selenium WebDriver
- **Design Pattern**: Page Object Model (POM)
- **Test Runner**: pytest
- **Reporting**: pytest-html
- **Screenshot**: Pillow

## Project Structure

```
Test Automation Project/
├── main.py                          # Main execution file
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── pages/                          # Page Object Model classes
│   ├── __init__.py
│   ├── home_page.py               # Homepage operations
│   ├── careers_page.py            # Careers page operations
│   └── qa_jobs_page.py            # QA Jobs page operations
├── tests/                          # Test files
│   ├── __init__.py
│   ├── base_test.py               # Base test class
│   └── test_insider_careers.py    # Main test scenarios
├── screenshots/                    # Screenshots taken when tests fail
└── test_results/                   # Test reports
```

## Installation

### Requirements
- Python 3.8 or higher
- Chrome browser
- pip (Python package manager)

### Steps

1. **Clone or download the project**

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Chrome WebDriver will be downloaded automatically** (thanks to webdriver-manager)

## Running Tests

### Run All Tests
```bash
python main.py
```

### Run Specific Test
```bash
python main.py test_01_homepage_navigation
python main.py test_complete_insider_careers_flow
```

### List Available Tests
```bash
python main.py --help
```

### Run Directly with Pytest
```bash
# All tests
pytest tests/ -v

# Specific test
pytest tests/test_insider_careers.py::test_01_homepage_navigation -v

# With HTML report
pytest tests/ -v --html=test_results/report.html --self-contained-html
```

## Test Reports

After tests are run:
- **HTML Reports**: in `test_results/` folder
- **Screenshots**: in `screenshots/` folder (when tests fail)

## Features

### POM (Page Object Model) Implementation
- Separate Page Object classes for each page
- Centralized locator management
- Reusable methods

### Error Handling
- Automatic screenshot capture (when tests fail)
- Detailed error messages
- Exception handling

### Wait Strategies
- Explicit Wait usage
- Element visibility control
- Clickability control

### Filtering and Verification
- Location-based filtering (Istanbul, Turkey)
- Department-based filtering (Quality Assurance)
- Job details verification
- Lever application form redirect verification

## Test Scenarios Detail

### 1. Homepage Test
- Opening Insider homepage
- Page title and URL verification

### 2. Careers Page Test
- Navigation to Careers page from Company menu
- Visibility of Locations, Teams, Life at Insider sections

### 3. QA Jobs Filtering Test
- Direct access to QA Jobs page
- Application of location and department filters
- Display of filtered results

### 4. Job Details Verification Test
- Each job listing containing "Quality Assurance"
- Accuracy of department information
- Location information being "Istanbul, Turkey"

### 5. Application Form Redirect Test
- Clicking "View Role" button
- Verification of redirect to Lever application form

## Troubleshooting

### Common Issues

1. **ChromeDriver Error**:
   - Ensure Chrome browser is up to date
   - webdriver-manager will automatically download appropriate driver

2. **Element Not Found Error**:
   - Check page loading times
   - Ensure locators are current

3. **Timeout Error**:
   - Check your internet connection
   - Increase page loading times

### Debug Mode
```bash
# Run with detailed output
pytest tests/ -v -s --tb=long
```

## Notes

- Tests run on the actual website
- Internet connection is required
- Tests should not be run in parallel
- Screenshots are taken automatically

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is developed for educational purposes.

---

**Note**: This test automation is developed according to the current structure of the Insider website. If there are changes in the site structure, locators may need to be updated. 