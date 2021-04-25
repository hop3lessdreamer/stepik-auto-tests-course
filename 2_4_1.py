from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os

link = 'https://suninjuly.github.io/explicit_wait2.html'

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.implicitly_wait(5)

	price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
	btn_1 = browser.find_element_by_id('book')
	btn_1.click()

	value = browser.find_element_by_id('input_value')
	value = value.text
	result = calc(value)
	input_1 = browser.find_element_by_id('answer')
	input_1.send_keys(result)

	btn_2 = browser.find_element_by_id('solve')
	browser.execute_script("return arguments[0].scrollIntoView(true);", btn_2)
	btn_2.click()

finally:
	time.sleep(12)
	browser.quit()