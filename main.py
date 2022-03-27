#!/usr/bin/python

import selenium
from selenium import webdriver
import time
import os,sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import math
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime
from time import sleep
import sys, traceback
import re    


## open the browser
##old one driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)


## open the zerodha
driver.get('https://www.jobware.de/')
driver.find_element_by_css_selector(".dsgvo-1B76C4DA4B-orange.dsgvo-1B76C4DA4B-accept").click()



pass_box = driver.find_element_by_xpath("//input[@placeholder='Stichwort, Jobtitel oder Firma']")
pass_box.send_keys("Software-Entwickler ")


pass_box = driver.find_element_by_xpath("//input[@placeholder='PLZ, Ort oder Land']")
pass_box.send_keys("Paderborn")

driver.find_element_by_xpath("//span[normalize-space()='Jobs finden']").click()


for i in range(5):
    if(i==0):
        driver.find_element_by_xpath("//body/jw-83hzo/section[@class='ng-star-inserted']/main[@class='ng-star-inserted']/div[@class='container']/div[@class='content']/div[@class='result']/div/div[2]/a[1]/div[2]").click()
        time.sleep(2.5)
        driver.switch_to.window(driver.window_handles[i+1]) 
        time.sleep(2.5)
        ##python
        ind=0
        for keyword in ['Pandas','Python','TensorFlow','Scikit-learn','SQL',]:
            get_source = driver.page_source 
            search_text = keyword
            if(search_text in get_source):
                ind+=1
        print(driver.current_url,"Matches: {}".format(ind))
 
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])    
    elif(i!=0):
        driver.find_element_by_xpath("//body/jw-83hzo/section[@class='ng-star-inserted']/main[@class='ng-star-inserted']/div[@class='container']/div[@class='content']/div[@class='result']/div/"+"div["+str(i+1)+"]/a[1]/div[1]/div[1]").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[i+1]) 
        time.sleep(2)
        ##python
        ind=0
        for keyword in ['Pandas','Python','TensorFlow','Scikit-learn','SQL']:
            get_source = driver.page_source 
            search_text =   keyword
            if(search_text in get_source):
                ind+=1
        print(driver.current_url,"Matches: {}".format(ind))
   
        driver.switch_to.window(driver.window_handles[0])    
        time.sleep(5)

time.sleep(10)


