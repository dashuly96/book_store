import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(20)
sel_ruby = driver.find_element_by_partial_link_text("Selenium Ruby")
sel_ruby.click()
time.sleep(20)
reviews = driver.find_element_by_css_selector(".reviews_tab")
reviews.click()
star = driver.find_element_by_css_selector(".star-5")
star.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
author = driver.find_element_by_id("author")
author.send_keys("Dasha")
email = driver.find_element_by_id("email")
email.send_keys("dashvol.spam@gmail.com")
submit = driver.find_element_by_id("submit")
submit.click()

driver.quit()