import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import random


class InternetSpeedTwitterBot:
    PROMISED_DOWN = 100
    PROMISED_UP = 60

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

        self.up = 0
        self.down = 0

        load_dotenv()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(3)
        # Depending on your location, you might need to accept the GDPR pop-up.
        accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        accept_button.click()

        sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        sleep(50)
        self.down = float(self.driver.find_element(By.XPATH,
                                                   value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]'
                                                         '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]'
                                                         '/span').text)

        self.up = float(self.driver.find_element(By.XPATH,
                                                 value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div'
                                                       '/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
                                                       '/span').text)

        print(f"[INFO] DOWNLOAD Mbps: {self.down}. UPLOAD Mbps: {self.up}")

    def login(self):
        self.driver.get("https://x.com")

        try:
            sleep(2)
            refuse_non_essential_cookies = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div'
                                                                              '/div/div/div/div[2]/button[2]')
            refuse_non_essential_cookies.click()
        except NoSuchElementException:
            pass

        sleep(2)
        login = self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
        login.click()

        sleep(4)
        phone_email_or_username = self.driver.find_element(By.NAME, "text")
        phone_email_or_username.send_keys(os.getenv("X_USERNAME"))

        sleep(2)
        next_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div"
                                                      "/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
        next_btn.click()

        self.simulate_human_login()

    def post(self):
        if self.down < self.PROMISED_DOWN or self.up < self.PROMISED_UP:
            try:
                sleep(2)
                what_s_happening = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div'
                                                                      '/div/div/div/div[3]/div/div[2]/div[1]/div/div'
                                                                      '/div/div[2]/div[1]/div/div/div/div/div/div/div'
                                                                      '/div/div/div/div/div[1]/div/div/div/div/div'
                                                                      '/div[2]/div/div/div/div')
                what_s_happening.send_keys(msg)
            except NoSuchElementException:
                pass

            sleep(5)
            tweet_compose = self.driver.find_element(By.XPATH,
                                                     value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div'
                                                           '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div'
                                                           '/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div'
                                                           '/div/div[2]/div/div/div/div')

            tweet = (f"Hey Internet Provider, why is my internet speed {self.down} Mbps download/{self.up} Mbps upload "
                     f"when I pay for {self.PROMISED_DOWN} download/{self.PROMISED_UP} upload?")

            tweet_compose.send_keys(tweet)
            sleep(3)

            tweet_button = self.driver.find_element(By.XPATH,
                                                    value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div'
                                                          '/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]'
                                                          '/div/div/div/button')
            tweet_button.click()

            sleep(2)

    def simulate_human_login(self):
        """Simulating Human Behavior with Selenium before Login btn click to Bypass reCAPTCHA.
        This method creates non-predictable Page Interaction Patterns using scrolling."""
        # Get total page height
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        current_scroll = 0

        try:
            sleep(2)
            phon_or_email = self.driver.find_element(By.NAME, "text")
            phon_or_email.send_keys(os.getenv("X_EMAIL"))
            phon_or_email.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

        sleep(2)
        phone_number_or_username = self.driver.find_element(By.NAME, "password")
        password = os.getenv("X_PASSWORD")

        # Fill a form field with delay
        for char in password:
            phone_number_or_username.send_keys(char)
            sleep(random.uniform(0.1, 0.3))  # Mimic typing delay

        while current_scroll < scroll_height:
            scroll_by = random.randint(100, 300)
            self.driver.execute_script(f"window.scrollBy(0, {scroll_by});")
            current_scroll += scroll_by
            sleep(random.uniform(0.5, 2.0))  # Random delay to mimic human reading/scanning

        # Find an element and simulate a human click
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div'
                                                       '/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div'
                                                       '/button')
        actions = ActionChains(self.driver)

        # Move to the element with a slight delay
        actions.move_to_element(login_btn).perform()
        sleep(random.uniform(0.5, 1.0))  # Pause before clicking
        login_btn.click()

    def exit(self):
        self.driver.quit()
