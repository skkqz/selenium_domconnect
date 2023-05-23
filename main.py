from selenium import webdriver
from selenium.webdriver.common.by import By

from config import email, password, input_email_xpath, input_password_xpath,\
    login_button_xpath, sing_in_path
import time


def login(browser):
    """Вход в личный кабинет пользователя"""

    browser.find_element(By.XPATH, sing_in_path).click()
    time.sleep(2)
    browser.find_element(By.XPATH, input_email_xpath).send_keys(email)
    browser.find_element(By.XPATH, input_password_xpath).send_keys(password)
    time.sleep(15)
    browser.find_element(By.XPATH, login_button_xpath).click()


def get_ip_proxy_and_expiration_date(browser):
    """Получение ip proxy и даты их окончания"""

    elements = browser.find_elements(By.TAG_NAME, 'tr')
    for i in elements[1:-2]:
        right_side = i.find_elements(By.CLASS_NAME, "right")
        ip_proxy = right_side[0].text
        end_of_proxy = right_side[6].text

        print(f'{ip_proxy} - {end_of_proxy}')


if __name__ in '__main__':

    browser = webdriver.Chrome()
    browser.get('https://proxy6.net/')
    login(browser)
    time.sleep(2)
    get_ip_proxy_and_expiration_date(browser)


