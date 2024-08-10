from selenium.webdriver.common.by import By
from faker import Faker
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import set_driver, authorize

fake = Faker()


def test_main_page_to_personal_cabinet_page(set_driver, authorize):
    driver = set_driver
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn)))
    driver.find_element(By.XPATH, Locators.personal_cabinet_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.exit_btn)))
    personal_cab_exit_btn = driver.find_element(By.XPATH, Locators.exit_btn)
    assert personal_cab_exit_btn.text == 'Выход'


def test_personal_cabinet_page_to_constructor_page(set_driver, authorize):
    driver = set_driver
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn)))
    driver.find_element(By.XPATH, Locators.personal_cabinet_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.exit_btn)))
    driver.find_element(By.XPATH, Locators.constructor_btn).click()
    constructor_title = driver.find_element(By.XPATH, Locators.constructor_title)
    assert constructor_title.text == 'Соберите бургер'


def test_personal_cabinet_exit_button(set_driver, authorize):
    driver = set_driver
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn)))
    driver.find_element(By.XPATH, Locators.personal_cabinet_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.exit_btn)))
    driver.find_element(By.XPATH, Locators.exit_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    login_title = driver.find_element(By.XPATH, Locators.enter_title)
    assert login_title.text == 'Вход'


def test_personal_cabinet_to_constructor_navigation_by_stellar_burger_logo_click(set_driver, authorize):
    driver = set_driver
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.personal_cabinet_btn)))
    driver.find_element(By.XPATH, Locators.personal_cabinet_btn).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.exit_btn)))
    driver.find_element(By.XPATH, Locators.stellar_burger_logo).click()
    constructor_title = driver.find_element(By.XPATH, Locators.constructor_title)
    assert constructor_title.text == 'Соберите бургер'