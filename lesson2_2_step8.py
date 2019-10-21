from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//label[contains(text(),'First name')]/following-sibling::input")
    input1.send_keys("Vasiliy")
    input2 = browser.find_element_by_xpath("//label[contains(text(),'Last name')]/following-sibling::input")
    input2.send_keys("Pupkin")
    input3 = browser.find_element_by_xpath("//label[contains(text(),'Email')]/following-sibling::input")
    input3.send_keys("Moscow@moscow.mos")
    input4 = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'thanks.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()