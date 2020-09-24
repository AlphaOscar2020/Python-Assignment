from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

contact_us_navigation_bar_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Contact Us')]")))
contact_us_navigation_bar_btn.click()

contact_page_header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-elem-id=1551634856822]/h1')))
assert contact_page_header.text == "Get in touch"

email_input_field = WebDriverWait(driver, 30).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("mail@example.com")

submit_btn = driver.find_element_by_class_name("tn-form__submit")
assert submit_btn.text == "SUBMIT"

submit_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "tn-form__submit")]')))
submit_btn.click()

home_pg_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='tn-atom' and text()='Home']")))
home_pg_btn.click()


driver.quit()

#Process finished with exit code 0