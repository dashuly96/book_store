import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

#проверка HTML5 Forms
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# time.sleep(20)
# email = driver.find_element_by_id("username")
# email.send_keys("dashvol.spam@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Reg123ister")
# login = driver.find_element_by_name("login")
# login.click()
# time.sleep(10)
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# time.sleep(10)
# driver.execute_script("window.scrollBy(0, 400);")
# html_5 = driver.find_element_by_partial_link_text("HTML5 Forms")
# html_5.click()
#
# title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "HTML5 Forms"))
# if title is False:
#     print("Заголовок не HTML5 Forms!")
# else:
#     print("Заголовок верный - HTML5 Forms.")

#проверка 3-х товаров в HTML
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# time.sleep(20)
# email = driver.find_element_by_id("username")
# email.send_keys("dashvol.spam@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Reg123ister")
# login = driver.find_element_by_name("login")
# login.click()
# time.sleep(20)
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# html = driver.find_element_by_css_selector(".cat-item.cat-item-19>a")
# html.click()
# time.sleep(10)
# products = driver.find_elements_by_tag_name("h3")
# if len(products) == 3:
#     print("На странице раздела HTML 3 товара")
# else:
#     print("Ошибка. На странице раздела HTML " + str(len(products)) + " товара")

#сортировка товаров
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# time.sleep(20)
# email = driver.find_element_by_id("username")
# email.send_keys("dashvol.spam@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Reg123ister")
# login = driver.find_element_by_name("login")
# login.click()
# time.sleep(20)
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
#
# sort = driver.find_element_by_css_selector("option:nth-child(1)")
# sort_default_selected = sort.get_attribute("selected")
# sort_default = sort.get_attribute("value")
# if sort_default == "menu_order" and sort_default_selected is not None:
#     print("Включена сортировка по умолчанию")
# else:
#     print("Включена сортировка не по умолчанию!")
#
# sort_desc = driver.find_element_by_css_selector(".orderby")
# select = Select(sort_desc)
# select.select_by_value("price-desc")
#
# sort = driver.find_element_by_css_selector("option:nth-child(6)")
# sort_default_selected = sort.get_attribute("selected")
# sort_default = sort.get_attribute("value")
# if sort_default == "price-desc" and sort_default_selected is not None:
#     print("Включена сортировка по цене от большей к меньшей")
# else:
#     print("Включена сортировка не по цене от большей к меньшей!")

#отображение, скидка товара
# my_account = driver.find_element_by_css_selector("#menu-item-50>a")
# my_account.click()
# time.sleep(20)
# email = driver.find_element_by_id("username")
# email.send_keys("dashvol.spam@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Reg123ister")
# login = driver.find_element_by_name("login")
# login.click()
# time.sleep(20)
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# time.sleep(20)
#
# android = driver.find_element_by_partial_link_text("Android Quick Start Guide")
# android.click()
# time.sleep(20)
#
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
#
# android_img = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")))
# android_img.click()
# close_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close_btn.click()

#проверка цены в корзине
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# time.sleep(20)
# add_to_basket = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
# add_to_basket.click()
# time.sleep(20)
#
# count = driver.find_element_by_css_selector(".cartcontents")
# count_text = count.text
# assert count_text == "1 Item"
#
# cost = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# cost_text = cost.text
# assert cost_text == "₹180.00"
#
# basket_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
# basket_btn.click()
# time.sleep(20)
#
# subtotal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal span")))
# total = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total span")))

#работа в корзине
# time.sleep(20)
# shop = driver.find_element_by_css_selector("#menu-item-40>a")
# shop.click()
# time.sleep(20)
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket_html5 = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
# add_to_basket_html5.click()
# time.sleep(20)
# add_to_basket_js = driver.find_element_by_css_selector(".post-180 a:nth-child(2)")
# add_to_basket_js.click()
# time.sleep(20)
#
# basket_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
# basket_btn.click()
# time.sleep(20)
#
# del_btn = driver.find_element_by_css_selector("[data-product_id='182']")
# del_btn.click()
# time.sleep(20)
# undo_btn = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo_btn.click()
# time.sleep(20)
#
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
# quantity.clear()
# quantity.send_keys("3")
#
# update_btn = driver.find_element_by_css_selector("[name='update_cart']")
# update_btn.click()
#
# quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
# quantity_value = quantity.get_attribute("value")
# assert int(quantity_value) == 3
#
# time.sleep(20)
# apply_btn = driver.find_element_by_css_selector("[name='apply_coupon']")
# apply_btn.click()
#
# error = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))

#покупка товара
time.sleep(20)
shop = driver.find_element_by_css_selector("#menu-item-40>a")
shop.click()
time.sleep(20)
driver.execute_script("window.scrollBy(0, 300);")

add_to_basket_html5 = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
add_to_basket_html5.click()
time.sleep(20)

basket_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
basket_btn.click()
time.sleep(20)

proceed_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
proceed_btn.click()

first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Dasha")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Voloshenenko")
email = driver.find_element_by_id("billing_email")
email.send_keys("dashvol.spam@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89876543211")

country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("Russia")
country_chosen = driver.find_element_by_css_selector(".select2-match")
country_chosen.click()

street = driver.find_element_by_id("billing_address_1")
street.send_keys("Street 1")
city = driver.find_element_by_id("billing_city")
city.send_keys("SPb")
state = driver.find_element_by_id("billing_state")
state.send_keys("SPb")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(20)
check_pay_btn = driver.find_element_by_id("payment_method_cheque")
check_pay_btn.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()

thanks = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
method = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))

driver.quit()