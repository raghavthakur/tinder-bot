from selenium import webdriver
from time import sleep
from account_info import email, password

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
        self.driver.switch_to_window(fb_login_popup)

        sleep(2)

        # enter email and password into text fields
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        sleep(2)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        
        sleep(2)
        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
