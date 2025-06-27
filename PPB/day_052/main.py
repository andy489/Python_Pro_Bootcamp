from dotenv import load_dotenv
from random import uniform
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
from time import sleep

SIMILAR_ACCOUNT = "nothing_4us"
MAX_FOLLOWS = 100
# ==== Load ENV Variables ====
load_dotenv()
INSTA_USER = os.getenv("INSTA_USER")
INSTA_PASS = os.getenv("INSTA_PASS")


def cooldown():
    wait = uniform(1, 2)
    print(f"[Cooldown] Sleeping for {wait:.2f} seconds...")
    sleep(wait)


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.driver.get("https://www.instagram.com/accounts/login/")
        cooldown()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "//button[contains(text(), 'Decline')]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(INSTA_USER)

        # Fill a form field with delay
        for char in INSTA_PASS:
            password.send_keys(char)
            sleep(uniform(0.1, 0.5))  # Mimic typing delay

        password.send_keys(Keys.ENTER)
        try:
            sleep(7)
            # Click "Not now" and ignore Save-login info prompt
            save_login_prompt = self.driver.find_element(by=By.XPATH, value="button[contains(text(), 'Decline')]")
            if save_login_prompt:
                save_login_prompt.click()
        except NoSuchElementException:
            input("Enter code on send to your WhatsApp manually and then press Enter to continue")

        sleep(8)
        try:
            # Click "not now" on notifications prompt
            notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
            if notifications_prompt:
                notifications_prompt.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        # Adding a hard sleep here to let the page full load after logging in
        sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        cooldown()

        self.followers_button = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                "//span[text()=' followers']")))
        self.followers_button.click()
        cooldown()

        # Locate scrollable div and scroll 5 times to load followers
        scrollable_popup = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                           '/html/body/div[4]/div[2]/div/div/div[1]/div'
                                                                           '/div[2]/div/div/div/div/div[2]/div/div'
                                                                           '/div[3]')))
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                       scrollable_popup)
            cooldown()

    def follow(self):
        # Find all follow buttons and click each; sleep in between actions
        follow_buttons = self.driver.find_elements(By.XPATH, '//div[text()="Follow"]')
        cooldown()
        counter = 0
        for button in follow_buttons:
            if counter > MAX_FOLLOWS:
                break
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                cooldown()
                button.click()
                counter = counter + 1
                cooldown()
            except Exception as e:
                print("Error clicking Follow button because: ", e)

    def exit(self):
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.exit()
