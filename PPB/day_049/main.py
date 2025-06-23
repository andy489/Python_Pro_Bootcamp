from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from dotenv import load_dotenv
import os

# LinkedIn Jobs: https://www.linkedin.com/jobs/jam/?showJobAlertsModal=false
# LinkedIn resume: Me (Profile Icon) -> Settings & Privacy -> Data privacy -> Job seeking preferences ->
# -> Job application settings > Upload resume

load_dotenv()

account_email = os.getenv("ACCOUNT_EMAIL")
account_password = os.getenv("ACCOUNT_PASSWORD")
account_phone = os.getenv("COUNTRY_CODE")
account_country_code = os.getenv("PHONE")

def abort_application():
    # Click Close Button
    close_btn = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_btn.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?"
    "distance=25"
    "&f_AL=true"
    "&f_WT=3%2C2"
    "&geoId=103835801"
    "&keywords=backend%20developer"
    "&origin=JOB_SEARCH_PAGE_JOB_FILTER"
    "&refresh=true"
    "&spellCorrectionEnabled=true"
    "&start=25"
)

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/section/div/div/div/div[2]/button")
sign_in_button.click()

# Sign in
time.sleep(2)
email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(account_email)
password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(account_password)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
description_names = ["Job title", "Company name", "Work Model"]
for listing in all_listings:
    print("Opening Listing:")
    description = listing.text.split("\n")

    for i in range(0, 3, 1):  # standard step of 1
        j = i
        if i > 0:
            j = i + 1
        print("\t" + description_names[i] + ": " + description[j])

    listing.click()
    time.sleep(3)

    try:
        # Click Easy Apply Button
        apply_button = driver.find_element(by=By.ID, value="jobs-apply-button-id")
        apply_button.click()
        time.sleep(2)

        # Insert Phone Number
        # Find an <input> dropdown element where the id contains phoneNumber-country
        country_code_dropdown = driver.find_element(by=By.CSS_SELECTOR, value="select[id*=phoneNumber]")
        select = Select(country_code_dropdown)
        current_selection = select.first_selected_option.text
        if current_selection == "Select an option":
            select.select_by_value(account_country_code)

        # Find an <input> element where the id contains phoneNumber
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        phone_value = phone.get_attribute("value")
        if phone_value == "":
            phone.send_keys(account_phone)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.text.strip().lower() == "next":
            print("Complex application, skipped.")
            abort_application()
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException as e:
        print("No application button, skipped.")
        continue

time.sleep(3)
driver.quit()