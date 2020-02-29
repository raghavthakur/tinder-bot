from selenium import webdriver
from time import sleep
from account_info import email, password
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')

        sleep(10) # pause 5 seconds for page to load

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup window
        base_window = self.driver.window_handles[0]
        fb_login_popup = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_login_popup)

        sleep(random.randint(1,4))

        # enter email and password into text fields
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        sleep(random.randint(1,4))

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        
        sleep(random.randint(1,4))
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        # switch to base window
        self.driver.switch_to.window(base_window)

        allow_location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location.click()
        allow_notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_notification.click()

        def like(self):
            like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_btn.click()

        
        def dislike(self):
            dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
            dislike_btn.click()




bot = TinderBot() # instantiate object
bot.login()