# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:16:23 2019

@author: LucasFranklin
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("http://www.python.org")

try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "start-shell"))
            )
finally:
    driver.quit()
    