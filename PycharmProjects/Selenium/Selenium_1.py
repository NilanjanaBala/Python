import time

from selenium import webdriver

driver = webdriver.Chrome("C://Users//Nilanjana Bala//Desktop//chromedriver_win32//chromedriver.exe")
driver.get("http://mytestinglabs.in/")
driver.find_element_by_name("email").send_keys("nilanjanabala14@gmail.com")
driver.find_element_by_id("sign-in").click()
time.sleep(5)
driver.find_element_by_id("email").send_keys("nilanjanabala14@gmail.com")
driver.find_element_by_name("password").send_keys("abc123")
driver.find_element_by_name("cnfpassword").send_keys("abc123")
driver.find_element_by_name("first_name").send_keys("Nilanjana")
driver.find_element_by_name("last_name").send_keys("Bala")
driver.find_element_by_class_name("username").send_keys("Nilanjana")
driver.find_element_by_id("textarea").send_keys("abc")
driver.find_element_by_id("agree").click()
driver.find_element_by_id("submitForm").click()


