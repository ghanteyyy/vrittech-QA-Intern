import os
import random
import string
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import otp


def generate_contact_number() -> str:
    digits = string.digits
    sample = random.sample(digits, k=8)

    return random.choice(['97', '98']) + ''.join(sample)


def fill_form(driver, form_contents) -> None:
    for label, value in form_contents.items():
        input_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, label))
        )
        input_box.click()
        input_box.send_keys(value)


def delay_click(driver, by, locator, timeout=15) -> None:
    wait = WebDriverWait(driver, timeout)

    for _ in range(3):
        try:
            element = wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
            return
        except StaleElementReferenceException:
            pass

    raise Exception("Failed to click element")



url = "https://authorized-partner.vercel.app/"
service = Service("./chromedriver-win64/chromedriver.exe")

options = Options()
options.binary_location = r"chrome-win64\chrome.exe"

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

# Navigating to "Set up your Account" form
delay_click(driver, By.XPATH, "//a[@href='/login']")
WebDriverWait(driver, 10).until(EC.url_contains("/login"))

delay_click(driver, By.XPATH, "//a[contains(@href,'register')]")
delay_click(driver, By.ID, "remember")
delay_click(driver, By.XPATH, "//button[normalize-space()='Continue']")

# Creating temporary email address
new_account = otp.create_account()

# Filling "Personal Details"
form1 = {
    "firstName": "Santosh",
    "lastName": "Karki",
    "email": new_account['email'],
    "phoneNumber": generate_contact_number(),
    "password": "M@dhumalla2",
    "confirmPassword": "M@dhumalla2",
}

fill_form(driver, form1)
delay_click(driver, By.XPATH, "//button[normalize-space()='Next']")

# Verifying OTP
_otp = otp.get_otp(new_account['token'])

otp_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-input-otp='true']"))
)

otp_input.click()

for o in _otp:
    otp_input.send_keys(o)

delay_click(driver, By.XPATH, "//button[normalize-space()='Verify Code']")

# Filling "Agency Details"
agency_name = ''.join(names.get_full_name().split())

form2 = {
    "agency_name": agency_name,
    "role_in_agency": "QA",
    "agency_email": f"{agency_name}@airsworld.net",
    "agency_website": f"www.{agency_name}.com",
    "agency_address": "Kathmandu, Nepal",
}

fill_form(driver, form2)

delay_click(driver, By.XPATH, "//button[@role='combobox' and .//span[contains(.,'Select Your Region of Operation')]]")
delay_click(driver, By.XPATH, "//div[@role='dialog']//div[.//span[normalize-space()='Australia']]")
delay_click(driver, By.XPATH, "//button[normalize-space()='Next']")

# Filling "Professional Experience"
delay_click(driver, By.XPATH, "//button[@role='combobox' and .//span[contains(.,'Select Your Experience Level')]]")
delay_click(driver, By.XPATH, "//span[normalize-space()='3 years']")

form3 = {
    "number_of_students_recruited_annually": str(random.randint(10, 100)),
    "focus_area": "Undergraduate admissions to Canada",
    "success_metrics": f"{random.randint(50, 100)}%"
}

fill_form(driver, form3)

check_buttons = ["Career Counseling", "Admission Applications", "Visa Processing", "Test Prepration"]
random.shuffle(check_buttons)

click_check_buttons = random.sample(check_buttons, k=random.randint(1, len(check_buttons)))

for ccb in click_check_buttons:
    delay_click(driver, By.XPATH, f"//label[normalize-space()='{ccb}']")

delay_click(driver, By.XPATH, "//button[normalize-space()='Next']")

# Filling "Verification and Preferences"
form4 = {
    "business_registration_number": ''.join(random.sample(string.digits, k=10)),
    "certification_details": "ICEF"
}

fill_form(driver, form4)

delay_click(driver, By.XPATH, "//button[@role='combobox' and .//span[contains(.,'Select Your Preferred Countries')]]")
delay_click(driver, By.XPATH, "//div[@role='dialog']//div[.//span[normalize-space()='Australia']]")

check_buttons = ["Universities", "Colleges", "Vocational School", "Other"]
random.shuffle(check_buttons)

click_check_buttons = random.sample(check_buttons, k=random.randint(1, len(check_buttons)))

for ccb in click_check_buttons:
    delay_click(driver, By.XPATH, f"//label[normalize-space()='{ccb}']")

file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")

for file_input in file_inputs:
    file_path = os.path.join(os.getcwd(), "Santosh_Kumar_Karki__QA_Intern.pdf")
    file_input.send_keys(file_path)

delay_click(driver, By.XPATH, "//button[normalize-space()='Submit']")


input("\n\nPress enter key to exit ...")

driver.quit()
