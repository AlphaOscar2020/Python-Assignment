import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

time.sleep(5)

contact_us_btn = driver.find_element_by_xpath('//div[contains(@class, "tn-elem__912597111551726675405")]')
contact_us_btn.click()

name_input_field = driver.find_element_by_name("Name")
name_input_field.send_keys("Adam First")

email_input_field = driver.find_element_by_name("Email")
email_input_field.send_keys("adam@example.com")

phone_input_field = driver.find_element_by_name("Phone")
phone_input_field.send_keys("+18474363041")

country_input_field = driver.find_element_by_name("Country")
country_input_field.send_keys("USA")

send_btn = driver.find_element_by_class_name("t-submit")
send_btn.click()

close_icon_btn = driver.find_element_by_xpath('//div[contains(@class, "t-popup__close-wrapper")]')
close_icon_btn.click()

time.sleep(5)

home_pg_btn = driver.find_element_by_xpath("//a[@class='tn-atom' and text()='Home']")
home_pg_btn.click()

driver.quit()

#Process finished with exit code 0
