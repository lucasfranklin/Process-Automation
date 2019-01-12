# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:56:54 2019

@author: LucasFranklin
"""

from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("file:///C:/Users/LucasFranklin/Desktop/Python Automation/Form.html")
username = driver.find_element_by_name('username')
print("My Login Form Element is:")
print(username)
driver.close()
