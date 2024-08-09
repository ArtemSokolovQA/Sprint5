from selenium.webdriver.common.by import By
from faker import Faker
from locators import Locators
from conftest import set_driver

fake = Faker()


def test_switch_to_bun_section(set_driver):
    driver = set_driver
    driver.get('https://stellarburgers.nomoreparties.site/')
    bun_button = driver.find_element(By.XPATH, Locators.bun_btn)
    assert 'current' in bun_button.get_attribute('class')


def test_switch_to_sauces_section(set_driver):
    driver = set_driver
    driver.get('https://stellarburgers.nomoreparties.site/')
    sauces_button = driver.find_element(By.XPATH, Locators.sauces_btn)
    sauces_button.click()
    assert 'current' in sauces_button.get_attribute('class')


def test_switch_to_fillings_section(set_driver):
    driver = set_driver
    driver.get('https://stellarburgers.nomoreparties.site/')
    fillings_button = driver.find_element(By.XPATH, Locators.fillings_btn)
    fillings_button.click()
    assert 'current' in fillings_button.get_attribute('class')