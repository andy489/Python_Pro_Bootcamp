from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# https://en.wikipedia.org/wiki/Main_Page

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(By.XPATH, value="//*[@id='articlecount']/ul/li[2]/a[1]")
# articles_count.click()

content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# https://secure-retreat-92358.herokuapp.com/

# driver.quit()

