import time
from selenium import webdriver

driver = webdriver.Chrome("/Users/nilanjana/SourceCode/Python/browser_driver/mac/chromedriver")
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element_by_xpath('//input[@name= "firstname"]').send_keys("ABC")
driver.find_element_by_xpath('//input[@name= "lastname"]').send_keys("XYZ")
driver.find_element_by_xpath('//input[contains(@aria-label, "Mobile number")]').send_keys("0000")
driver.find_element_by_xpath('//input[@type= "password"]').send_keys("123")


