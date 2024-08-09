from selenium.webdriver.common.by import By
from faker import Faker
import data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import set_driver

fake = Faker()


def test_positive_success_register(set_driver):
    driver = set_driver
    driver.get(data.REGISTER_URL)
    driver.find_element(By.XPATH, Locators.register_name_input).send_keys(fake.name()[:5])
    driver.find_element(By.XPATH, Locators.register_email_input).send_keys(fake.email())
    driver.find_element(By.XPATH, Locators.register_password_input).send_keys(fake.password())
    driver.find_element(By.XPATH, Locators.register_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.enter_title)))
    authorization_page_title_text = driver.find_element(By.XPATH, Locators.enter_title).text
    assert authorization_page_title_text == 'Вход'


def test_register_with_5symbols_in_password(set_driver):
    driver = set_driver
    driver.get(data.REGISTER_URL)
    driver.find_element(By.XPATH, Locators.register_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, Locators.register_email_input).send_keys(fake.email())
    driver.find_element(By.XPATH, Locators.register_password_input).send_keys(fake.password(length=5))
    driver.find_element(By.XPATH, Locators.register_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.wrong_password_alert)))
    authorization_page_title_text = driver.find_element(By.XPATH, Locators.wrong_password_alert).text
    assert authorization_page_title_text == 'Некорректный пароль'