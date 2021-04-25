from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector('form .nowrap#input_value')
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector('input#answer')
	input1.send_keys(y)

	rdbtn1 = browser.find_element_by_css_selector('#robotCheckbox')
	rdbtn1.click()
	chbtn1 = browser.find_element_by_css_selector('#robotsRule')
	chbtn1.click()
	btn1 = browser.find_element_by_css_selector("button[type='submit']")
	btn1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()