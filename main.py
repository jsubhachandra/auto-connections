import time
from random import randrange

import sentry_sdk
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

import settings


MESSAGE_TEXT = """Hi

I hope you are doing well. I would like to connect with you on LinkedIn to exchange professional views, experiences, and information.

Thanks!
"""


class LinkedIn:
    def __init__(self):
        sentry_sdk.init(settings.SENTRY_SDK, traces_sample_rate=1.0)
        self.options = Options()
        self.landing_url = settings.LINKEDIN_LANDING_URL
        self.chromedriver_path = settings.CHROMEDRIVER_PATH
        self.search_url = settings.LINKEDIN_SEARCH_URL

        # Update the search url with dynamic page numbers to get maximum invitations possible everytime the script runs
        self.search_url = f'{self.search_url[:-1]}{randrange(10)}'

        self.username = settings.USERNAME
        self.password = settings.PASSWORD
        self.counter = 0
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')

        if not settings.DEBUG:
            self.options.add_argument('--headless')

        if self.chromedriver_path:
            self.driver = webdriver.Chrome(self.chromedriver_path, chrome_options=self.options)
        else:
            self.driver = webdriver.Chrome(chrome_options=self.options)

        self.driver.set_window_size(1366, 768)

    def send_connection_requests(self):
        self.driver.get(self.landing_url)
        print("Opening landing page")
        time.sleep(3)
        self.driver.find_element_by_id("username").send_keys(self.username)
        password_field = self.driver.find_element_by_id("password")
        password_field.send_keys(self.password)
        print("Password entered")
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
        print("Logging in")
        time.sleep(2)
        self.driver.get(self.search_url)
        print("Opening search page")
        time.sleep(3)
        all_button_spans = self.driver.find_elements_by_class_name('artdeco-button__text')
        for button_span in all_button_spans:
            if button_span.text == 'Connect':
                button_span.find_element_by_xpath("./..").click()
                print("Clicked connect button")
                time.sleep(2)
                self.driver.find_element_by_xpath('//button[@aria-label="Add a note"]').click()
                self.driver.find_element_by_tag_name("textarea").send_keys(MESSAGE_TEXT)

                send_button = self.driver.find_element_by_css_selector("button[aria-label='Send now']")
                send_button.click()
                self.counter += 1
                print(f"{self.counter} invitation sent")
                time.sleep(2)


if __name__ == '__main__':
    counter = 0
    total_invitations = 0

    """
    Iterate the whole process 15 times because of a known bug with chromedriver and memory issue.
    """
    while counter < 15:
        print(f"\n{counter} try ............")
        obj = LinkedIn()
        try:
            obj.send_connection_requests()
        except WebDriverException:
            obj.driver.quit()
            counter += 1
        else:
            total_invitations = obj.counter
            obj.driver.quit()
            break

    print(f"Total {total_invitations} invitations sent.")
