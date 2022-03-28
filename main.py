#!/usr/bin/python

## selenium libraries
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
from selenium.common.exceptions import TimeoutException


## mail sending librariers
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, traceback
import re    

# time libraries
from datetime import datetime
from time import sleep



## opens the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)

## open the jobware site
driver.get('https://www.jobware.de/')
driver.find_element_by_css_selector(".dsgvo-1B76C4DA4B-orange.dsgvo-1B76C4DA4B-accept").click()

## job name
pass_box = driver.find_element_by_xpath("//input[@placeholder='Stichwort, Jobtitel oder Firma']")
pass_box.send_keys(input("Enter the job title : "))

## location
pass_box = driver.find_element_by_xpath("//input[@placeholder='PLZ, Ort oder Land']")
pass_box.send_keys(input("Enter the location : "))

##search
driver.find_element_by_xpath("//span[normalize-space()='Jobs finden']").click()

keywords=input("Enter the keywords (with space no comma) : ").split()


print("  ")
print("  ")
## no of positions
for i in range(1,10):
    if(1):
        try:
            driver.find_element_by_xpath("//body/jw-83hzo/section[@class='ng-star-inserted']/main[@class='ng-star-inserted']/div[@class='container']/div[@class='content']/div[@class='result']/div/"+"div["+str(i+1)+"]/a[1]/div[1]/div[1]").click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1]) 
            time.sleep(2)
            ##python
            ind=0
            for keyword in keywords:
                get_source = driver.page_source 
                if(keyword.upper() in get_source or keyword.lower() in get_source or keyword.title() in get_source):
                    ind+=1
            print("Matches: {}".format(ind), driver.current_url)
            print("  ")
            driver.close()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[0])    
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except :
            pass
time.sleep(10)

