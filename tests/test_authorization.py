from selenium.webdriver.common.by import By
from faker import Faker

import data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import set_driver

fake = Faker()


def test_login_button_on_home_page(set_driver):
    driver = set_driver
    driver.get(data.LOGIN_URL)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.login_email_input).send_keys('artem_sokolov_12_666@yandex.ru')
    driver.find_element(By.XPATH, Locators.login_password_input).send_keys('practicum')
    driver.find_element(By.XPATH, Locators.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn))).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.exit_btn)))
    assert driver.find_element(By.XPATH, Locators.exit_btn).text == 'Выход'


def test_login_button_on_personal_cabinet(set_driver):
    driver = set_driver
    driver.get(data.LOGIN_URL)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.login_email_input).send_keys('artem_sokolov_12_666@yandex.ru')
    driver.find_element(By.XPATH, Locators.login_password_input).send_keys('practicum')
    driver.find_element(By.XPATH, Locators.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.make_order_btn)))
    assert driver.find_element(By.XPATH, Locators.make_order_btn).text == 'Оформить заказ'


def test_login_button_on_registration_form(set_driver):
    driver = set_driver
    driver.get(data.LOGIN_URL)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.login_email_input).send_keys('artem_sokolov_12_666@yandex.ru')
    driver.find_element(By.XPATH, Locators.login_password_input).send_keys('practicum')
    driver.find_element(By.XPATH, Locators.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.make_order_btn)))
    assert driver.find_element(By.XPATH, Locators.make_order_btn).text == 'Оформить заказ'


def test_login_button_on_restore_password_form(set_driver):
    driver = set_driver
    driver.get(data.LOGIN_URL)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.restore_password_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.restore_password_form_login_btn)))
    driver.find_element(By.XPATH, Locators.restore_password_form_login_btn).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.login_email_input).send_keys('artem_sokolov_12_666@yandex.ru')
    driver.find_element(By.XPATH, Locators.login_password_input).send_keys('practicum')
    driver.find_element(By.XPATH, Locators.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.make_order_btn)))
    assert driver.find_element(By.XPATH, Locators.make_order_btn).text == 'Оформить заказ'