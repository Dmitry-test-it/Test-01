from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # новый коммит 2

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
