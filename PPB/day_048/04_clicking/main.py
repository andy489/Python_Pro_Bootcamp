from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]")
# article_count.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
