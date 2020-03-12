from selenium import webdriver
import os
import time
from time import sleep
from multiprocessing import Process
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Process


class InstagramBot:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')
        self.base_url = 'https://www.instagram.com'

        self.driver.get('{}/accounts/login/'.format(self.base_url))
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base_url, user))
        sleep(2)

    def see_followers(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(1)

    def actively_follow(self):
        follow = self.driver.find_elements_by_class_name('sqdOP')
        for x in follow:
            x.click()
            sleep(2)

    def scroll(self):

        scroll_pause_time = 5

        while True:
            screen = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
            #THIS IS ORIGINAL: self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", screen)
            self.driver.execute_script("arguments[0].scrollBy(0, 100)", screen)
    
            sleep(scroll_pause_time)
        


    if __name__ == '__main__':
        p1 = Process(target=actively_follow)
        p1.start()
        p2=Process(target=scroll)
        p2.start()









if __name__ == '__main__':
    ig_bot = InstagramBot ('YOUR_USERNAME', 'YOUR_PASSWORD')
    ig_bot.nav_user('THE_ACCOUNT_USERNAME')
    ig_bot.see_followers()
    ig_bot.actively_follow()
    ig_bot.scroll()
