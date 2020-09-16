import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://datafolks.com/")

time.sleep(5)
home = driver.find_element_by_xpath('//div[@data-elem-id=1551634462374]/a')
assert home.text == "Home"

portfolio = driver.find_element_by_xpath('//div[@data-elem-id=1551634481382]/a')
assert portfolio.text == "Portfolio"

services = driver.find_element_by_xpath('//div[@data-elem-id=1551634484712]/a')
assert services.text == "Services"

ContactUs = driver.find_element_by_xpath('//div[@data-elem-id=1551634487768]/a')
assert ContactUs.text == "Contact Us"

driver.quit()