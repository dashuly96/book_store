import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

#проверка регистрации
my_account = driver.find_element_by_css_selector("#menu-item-50>a")
my_account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("dashvol.spam@gmail.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("Reg123ister")
register = driver.find_element_by_name("register")
register.click()

#проверка авторизации
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# time.sleep(20)
# email = driver.find_element_by_id("username")
# email.send_keys("dashvol.spam@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Reg123ister")
# login = driver.find_element_by_name("login")
# login.click()
# logout = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, "Logout"), "Logout"))
# if logout is False:
#     print("Элемента Logout нет!")
# else:
#     print("Элемент Logout на месте.")

driver.quit()