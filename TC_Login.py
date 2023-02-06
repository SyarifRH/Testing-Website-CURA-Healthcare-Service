from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def test_valid_login():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_valid_login()


def test_invalid_login_username():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('InvalidUsername')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_username()


def test_invalid_login_password():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('InvalidPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_password()


def test_invalid_login_none():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_none()


def test_invalid_login_empty_username():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('ThisIsNotAPassword')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_empty_username()


def test_invalid_login_empty_password():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John Doe')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_empty_password()


def test_invalid_login_specialCaracther():
    driver = webdriver.Chrome()
    url_login = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(url_login)
    menu = driver.find_element(By.XPATH, "//a[@id='menu-toggle']/i")
    menu.click()
    login = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
    login.click()
    username_input = driver.find_element(
        By.XPATH, "//input[@id='txt-username']")
    username_input.send_keys('John!@#$%^&()_+')
    password_input = driver.find_element(
        By.XPATH, "//input[@id='txt-password']")
    password_input.send_keys('Doe!@#$%^&()_+')
    access_login = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    access_login.click()
    time.sleep(2)
    driver.quit()


test_invalid_login_specialCaracther()
