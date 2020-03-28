import time
from Login_page import login

driver = login()
driver.find_element_by_xpath("//span[text()='Gadgets']").click()
driver.find_element_by_xpath('//a[contains(@href,"calendar")]').click()
calendar_input = driver.find_element_by_xpath('//input[@placeholder="Date of birth"]')
calendar_input.clear()
calendar_input.send_keys("03/14/1988")