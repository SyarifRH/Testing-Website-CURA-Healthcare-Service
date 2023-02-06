from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url_login = ('https://www.saucedemo.com/')
driver.get(url_login)

username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
username_input.send_keys('standard_user')
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys('secret_sauce')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
time.sleep(10)
driver.exit()
