# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:39:14 2019

@author: LucasFranklin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("http://wiki.python.org/moin/FrontPage")

searchbox = driver.find_element_by_id("searchinput")
searchbox.send_keys("Begginer")
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
select = Select(driver.find_element_by_xpath("//*/form/div/select"))
select.select_by_visible_text("Raw Text")