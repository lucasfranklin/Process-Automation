# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:19:29 2019

@author: LucasFranklin
"""
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("file:///C:/Users/LucasFranklin/Desktop/Python Automation/Form.html")
content = driver.find_element_by_class_name("content")

print("This is my content id: ")
print(content)

driver.close()
