from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Fill form
# Test URL: https://secure-retreat-92358.herokuapp.com/
# Find the first name, last name, and email fields
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Andrey")
last_name.send_keys("Stoev")
email.send_keys("stoev.andy@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

driver.quit()