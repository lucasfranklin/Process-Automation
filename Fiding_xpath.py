# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:59:04 2019

@author: LucasFranklin
"""

from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("file:///C:/Users/LucasFranklin/Desktop/Python Automation/Form.html")
login_form_abs = driver.find_element_by_xpath("/html/body/form[1]")
login_form_rel = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")


print("My ABS Login Form Element is:")
print(login_form_abs)
print("My REL Login Form Element is:")
print(login_form_rel)
print("My ABS Login Form Element is:")
print(login_form_abs)
print("My ID Login Form Element is:")
print(login_form_id)
driver.close()
