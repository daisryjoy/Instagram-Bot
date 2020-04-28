from selenium import webdriver
from time import sleep
from secrets import pw
import os 

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(r'C:\Users\daisr\OneDrive\Documents\Code\unfollowed\chromedriver_win32\chromedriver.exe')
        self.username = username

        self.driver.get("https://www.instagram.com/")
        sleep(2)

        #login button 
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]')\
        #    .click()
        #username 
        #login_field = 
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)
        #password 
        #login_field = 
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(pw)
        #login button ?
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        #Turn off notifications: Not Now button
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(5)


    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        #self.driver.find_element_by_xpath("//a[contains@href, '/following')]")\
        #    .click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
            .click()
        sleep(5)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]') 
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        last_ht, ht = 0, 1
        while last_ht != ht: 
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)


my_bot = InstaBot('joy.ladignon', pw)
my_bot.get_unfollowers()