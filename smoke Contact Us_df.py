from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

contact_us_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Contact Us')]")))
contact_us_btn.click()

email_input_field = WebDriverWait(driver, 30).until((EC.visibility_of_element_located((By.XPATH, "//form[@id='form91499566']/div[2]/div[1]/div[2]/input[1]"))))
email_input_field.send_keys("mail@example.com")

submit_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "tn-form__submit")]')))
submit_btn.click()

home_pg_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='tn-atom' and text()='Home']")))
home_pg_btn.click()


driver.quit()


#Process finished with exit code 0

