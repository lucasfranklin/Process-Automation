# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:22:48 2019

@author: LucasFranklin
"""

from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.implicitly_wait(10)

driver.get("http://www.python.org")

myDynamicElement = driver.find_element_by_id("start-shell")

driver.close()