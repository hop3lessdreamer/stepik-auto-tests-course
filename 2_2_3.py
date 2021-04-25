from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = 'https://suninjuly.github.io/file_input.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	f_name = browser.find_element_by_css_selector('input[name="firstname"]')
	f_name.send_keys('name')

	l_name = browser.find_element_by_css_selector('input[name="lastname"]')
	l_name.send_keys('name')

	email = browser.find_element_by_css_selector('input[name="email"]')
	email.send_keys('em@ad.sy')

	file = browser.find_element_by_id('file')
	path_to_file = os.path.abspath(os.path.dirname(__file__)) + '\\2_2_3.txt'
	file.send_keys(path_to_file)

	btn = browser.find_element_by_css_selector('button[type="submit"]')
	btn.click()

finally:
	time.sleep(7)
	browser.quit()