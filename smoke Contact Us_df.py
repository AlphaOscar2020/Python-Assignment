from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

contact_us_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "tn-elem__912597111551726675405")]')))
contact_us_btn.click()

name_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Name")))
name_input_field.send_keys("Adam First")

email_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Email")))
email_input_field.send_keys("adam@example.com")

phone_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Phone")))
phone_input_field.send_keys("+18474363041")

country_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Country")))
country_input_field.send_keys("USA")

send_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "t-submit")))
send_btn.click()

close_icon_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "t-popup__close-wrapper")]')))
close_icon_btn.click()

home_pg_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='tn-atom' and text()='Home']")))
home_pg_btn.click()

driver.quit()

#Process finished with exit code 0