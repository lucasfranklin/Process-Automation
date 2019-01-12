# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:42:09 2019

@author: LucasFranklin
"""

from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("file:///C:/Users/LucasFranklin/Desktop/Python Automation/Form.html")
login_form = driver.find_element_by_id('loginForm')
print("My Login Form Element is:")
print(login_form)
driver.close()
