from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	btn = browser.find_element_by_css_selector('button[type="submit"]')
	btn.click()

	wndw = browser.switch_to.alert
	wndw.accept()

	value = browser.find_element_by_id('input_value')
	value = value.text
	result = calc(value)

	answ = browser.find_element_by_id('answer')
	answ.send_keys(result)

	btn_smt = browser.find_element_by_css_selector('button[type="submit"]')
	btn_smt.click()

finally:
	time.sleep(7)
	browser.quit()