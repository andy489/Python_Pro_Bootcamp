from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium documentation: https://selenium-python.readthedocs.io/

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")

price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is ${price_whole.text}.{price_fraction.text}")

# driver.close() # closes a single tab (the active tab)
driver.quit() # closes the entire browser
