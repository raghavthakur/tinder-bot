from selenium import webdriver
from time import sleep
from account_info import email, password
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5) # pause 5 seconds for page to load

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

        sleep(5) # pause 5 seconds for page to load

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

    # TODO: Add logic for dislike
    def auto_swipe(self):
        while True:
            sleep(random.randint(3,6))
            # finite-state machine
            try:
                self.like()
            except Exception: # if cannot click like try closing popups
                try:
                    self.close_add_home_screen_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_out_of_likes_popup()



    def close_add_home_screen_popup(self):
            add_home_screen = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            add_home_screen.click()

    def close_out_of_likes_popup(self):
            out_of_likes = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            out_of_likes.click()

    def close_match(self):
            keep_swiping = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            keep_swiping.close()


bot = TinderBot() # instantiate object
bot.login()
bot.auto_swipe()
