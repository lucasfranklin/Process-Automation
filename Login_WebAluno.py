# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:16:22 2019

@author: LucasFranklin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("http://webgiz.unimontes.br/")

username = driver.find_element_by_name("username")
username.clear()
username.send_keys("0208057")
time.sleep(3)
password = driver.find_element_by_name("passwd")
password.clear()
password.send_keys("******")
time.sleep(3)
login = driver.find_element_by_id("btnlogin")
login.click()
