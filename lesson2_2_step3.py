from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

import math

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    a = (int)(browser.find_element_by_id("num1").text)
    b = (int)(browser.find_element_by_id("num2").text)
    c = a + b
    c = (str)(c)
    print(c)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(c)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
