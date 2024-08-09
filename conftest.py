import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def set_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def authorize(set_driver):
    driver = set_driver  # Используем уже созданный объект WebDriver
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, Locators.main_page_login_btn).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    driver.find_element(By.XPATH, Locators.login_email_input).send_keys('artem_sokolov_12_666@yandex.ru')
    driver.find_element(By.XPATH, Locators.login_password_input).send_keys('practicum')
    driver.find_element(By.XPATH, Locators.login_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn)))
    return driver

