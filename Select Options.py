# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:42:10 2019

@author: LucasFranklin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("file:///C:/Users/LucasFranklin/Desktop/Python Automation/Form2.html")

selector = Select(driver.find_element_by_name('numReturnSelect'))
selector.select_by_index(4)
selector.select_by_visible_text("200")
selector.select_by_value("250")

print(selector.options)

submit_button = driver.find_element_by_name("continue")
submit_button.submit()