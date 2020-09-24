import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

see_why_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-elem-id=1551635176282]')))
see_why_btn.click()

time.sleep(20)

driver.quit()

#Process finished with exit code 0