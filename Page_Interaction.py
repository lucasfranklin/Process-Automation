# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:32:59 2019

@author: LucasFranklin
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://www.python.org")

searchbox = driver.find_element_by_name('q')
searchbox.clear()
searchbox.send_keys("pycon")
searchbox.send_keys(Keys.RETURN)
