from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os

link = ''

try:
	browser = webdriver.Chrome()
	browser.get(link)



finally:
	time.sleep(10)
	browser.quit()