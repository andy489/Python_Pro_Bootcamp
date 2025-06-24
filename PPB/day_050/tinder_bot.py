from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import random
from dotenv import load_dotenv
import os


class TinderAutoSwipe:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        load_dotenv()
        self.fb_email = os.getenv("FB_EMAIL")
        self.fb_pass = os.getenv("FB_PASSWORD")
        self.phone = os.getenv("PHONE")

    def simulate_human_behaviour(self):
        """Simulating Human Behavior with Selenium before Login btn click to Bypass reCAPTCHA.
        This method creates non-predictable Page Interaction Patterns using scrolling."""
        # Get total page height
        total_height = self.driver.execute_script("return document.body.scrollHeight")

        # Set viewport to appear at bottom without animation
        self.driver.execute_script(f"window.scrollTo(0, {total_height});")

        # Move to element then scroll down in small increments
        for _ in range(7):
            random_pos = random.randint(0, total_height)
            self.driver.execute_script(f"window.scrollTo(0, {random_pos});")
            sleep(random.uniform(0.3, 1.5))

    def login(self):
        self.driver.get("http://www.tinder.com")

        sleep(3)
        accept_cookies = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]'
                                                                  '/button')
        accept_cookies.click()

        sleep(2)
        login_button = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
        login_button.click()

        sleep(2)
        fb_login = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[2]'
                                                            '/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
        fb_login.click()

        sleep(2)
        base_window = self.driver.window_handles[0]
        fb_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_login_window)
        print(self.driver.title)

        sleep(2)

        cookies_button = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div/div/div/div/div[3]'
                                                                  '/div[2]/div/div[1]/div[2]/div')
        cookies_button.click()

        sleep(2)
        # Facebook Login
        email = self.driver.find_element(By.XPATH, value='//*[@id="email"]')
        password = self.driver.find_element(By.XPATH, value='//*[@id="pass"]')
        email.send_keys(self.fb_email)
        password.send_keys(self.fb_pass)

        sleep(1)

        self.simulate_human_behaviour()

        password.send_keys(Keys.ENTER)

        sleep(5)

        continue_as_me = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div/div/div/div[1]'
                                                                  '/div[3]/div/div/div/div/div/div/div/div/div[3]'
                                                                  '/div[1]/div/div/div/div[1]/div/div/div/div')
        continue_as_me.click()

        sleep(5)

        self.driver.switch_to.window(base_window)
        print(self.driver.title)
        input_phone = self.driver.find_element(By.ID, "phone_number")
        input_phone.send_keys(self.phone)
        input_phone.send_keys(Keys.ENTER)

        sleep(3)

        self.driver.switch_to.window(base_window)
        input("Click \"Start Puzzle\" and complete a challenge manually to verify you're a human.\n"
              "Enter the code sent to your phone via message and manually click \"Next\".\n"
              "Then press Enter in the IDE's terminal to pass the control to the Selenium driver again.")

        sleep(2)

        allow_btn = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
        allow_btn.click()

        sleep(2)

        # Turn on notifications
        i_will_give_it_a_miss_btn = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div/div'
                                                                             '/div[3]/button[2]')
        i_will_give_it_a_miss_btn.click()

        sleep(4)

    def swipe(self):
        # Tinder free tier only allows 100 "Likes" per day.
        for _ in range(100):
            # Add a 1s delay between likes.
            sleep(2)
            try:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_RIGHT)
                actions.perform()
            # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
            except ElementClickInterceptedException:
                try:
                    add_tinder_to_home_screen = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div'
                                                                                   '/div[2]/button[2]')
                    add_tinder_to_home_screen.click()
                except NoSuchElementException:
                    pass

                try:
                    match_popup = self.driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                    match_popup.click()
                # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
                except NoSuchElementException:
                    sleep(2)

    def exit(self):
        self.driver.quit()
