from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	value_selector = browser.find_element_by_id('treasure')
	value = value_selector.get_attribute('valuex')

	result = calc(value)

	input_answ = browser.find_element_by_css_selector('#answer')
	input_answ.send_keys(result)

	chbtn = browser.find_element_by_id('robotCheckbox')
	chbtn.click()

	rdbtn = browser.find_element_by_id('robotsRule')
	rdbtn.click()

	bnt_smbt = browser.find_element_by_css_selector('button[type="submit"]')
	bnt_smbt.click()

finally:
	time.sleep(10)
	browser.quit()