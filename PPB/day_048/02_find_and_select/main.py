from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")  # selenium element not html
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

submit_btn = driver.find_element(By.ID, value="submit")
print(submit_btn.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# XPath: https://www.w3schools.com/xml/xpath_intro.asp
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_attribute("href"))

driver.quit()
