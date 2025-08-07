from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def fetch_case_details(case_type, case_number, filing_year):
    options = Options()
    options.add_argument("--headless")  # Run in background; remove to see browser
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://services.ecourts.gov.in/ecourtindia_v6/"
        driver.get(url)
        time.sleep(2)

        # Click on "Case Status"
        case_status_link = driver.find_element(By.LINK_TEXT, "Case Status")
        case_status_link.click()
        time.sleep(2)

        return {
            "status": "Successfully loaded the eCourts website and opened Case Status page. Now ready to fill form."
        }

    except Exception as e:
        return {"error": str(e)}

    fin

