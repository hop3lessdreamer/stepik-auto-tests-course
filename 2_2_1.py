from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
	link = "https://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element_by_id('num1')
	num1 = int(num1.text)

	num2 = browser.find_element_by_id('num2')
	num2 = int(num2.text)

	s = num1 + num2

	lst = Select(browser.find_element_by_tag_name("select"))
	lst.select_by_visible_text(str(s))

	btn = browser.find_element_by_css_selector('button[type="submit"]')
	btn.click()

finally:
	time.sleep(7)
	browser.quit()