import json
from dataclasses import dataclass
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import sys
import time

# baca file json


def read_credentials():
    secrets = 'secrets.json'
    with open(secrets) as f:
        keys = json.loads(f.read())
        return keys


class SIMkuliah:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.base_url = "https://simkuliah.unsyiah.ac.id"
        # self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.COMMAND_OR_CONTROL = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

    def single_interation_over_session(self):
        self.login_to_simkuliah()
        time.sleep(5)
        self.driver.quit()

    def login_to_simkuliah(self):
        self.driver.get(self.base_url)
        self.put_credentials_to_form()
        self.get_to_absen_simkuliah()

    def put_credentials_to_form(self):
        try:
            # Enter user credentials and Click on Submit button to Logins
            self.driver.find_element_by_name("username").send_keys(self.login)
            time.sleep(2)
            password_field = self.driver.find_element_by_name("password")
            password_field.send_keys(self.password)
            password_field.submit()
            time.sleep(3)

        except NoSuchElementException:
            print("Exception NoSuchElementException")

    def get_to_absen_simkuliah(self):
        try:
            self.driver.find_element_by_link_text('Python').click()
            time.sleep(2)
        except NoSuchElementException:
            print("Absen Belum ada")
        pass


if __name__ == '__main__':
    credentials = read_credentials()
    bot = SIMkuliah(credentials.get('username'),
                    credentials.get('password'))
    bot.single_interation_over_session()
