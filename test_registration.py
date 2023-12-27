import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):

    def test_one(self):

        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Код, который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        name.send_keys("Ivan")
        second_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        second_name.send_keys("Ivanov")

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        email.send_keys('ivanych777')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_two(self):

        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Код, который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        name.send_keys("Ivan")
        second_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        second_name.send_keys("Ivanov")

        email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        email.send_keys('ivanych777')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
