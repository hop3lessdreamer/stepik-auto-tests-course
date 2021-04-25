from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)

	btn_1 = browser.find_element_by_css_selector('button[type="submit"]')
	btn_1.click()

	windows = browser.window_handles

	second_window = windows[1]
	browser.switch_to.window(second_window)
	time.sleep(1)

	value = browser.find_element_by_id('input_value')
	value = value.text
	result = calc(value)
	print(result)

	answ = browser.find_element_by_id('answer')
	answ.send_keys(result)

	btn_2 = browser.find_element_by_css_selector('button[type="submit"]')
	btn_2.click()


finally:
	time.sleep(7)
	browser.quit()
