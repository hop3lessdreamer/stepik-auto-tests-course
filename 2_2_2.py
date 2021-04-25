from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_id('input_value')
	x = x.text
	result = calc(x)

	answ = browser.find_element_by_id('answer')
	answ.send_keys(result)


	chbtn = browser.find_element_by_id('robotCheckbox')
	chbtn.click()

	rdbtn = browser.find_element_by_id('robotsRule')
	browser.execute_script("return arguments[0].scrollIntoView(true);", rdbtn)
	rdbtn.click()
	btn = browser.find_element_by_css_selector('button[type="submit"]')
	btn.click()

finally:
	time.sleep(7)
	browser.quit()