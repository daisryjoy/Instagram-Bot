from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import pw
import os 

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(r'C:\Users\daisr\OneDrive\Documents\Code\unfollowed\chromedriver_win32\chromedriver.exe')
        self.username = username

        self.driver.get("https://www.instagram.com/")
        sleep(2)

        #username 
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)

        #password 
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(pw)

        #login button 
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)

        #Turn off notifications: Not Now button
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(5)
    
   def get_unfollowers(self):
        #click user profile
        #self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
        #    .click()

        self.driver.find_element_by_link_text(self.username)\
            .click()
        sleep(5)

        #following
        self.driver.find_element_by_class_name('g47SY')\
            .click()

        
        sleep(5)
        #click on following
        
my_bot = InstaBot('joy.ladignon', pw)
my_bot.get_unfollowers()

