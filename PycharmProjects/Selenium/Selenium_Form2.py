import time

from Login_page import login

driver = login()
driver.find_element_by_xpath("//span[text()='Registration Form']").click()
driver.find_element_by_xpath('//a[contains(@href,"formTwo")]').click()
time.sleep(2)
driver.find_element_by_xpath('//input[@placeholder="Enter email"]').send_keys("nilanjanabala14@gmail.com")
driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("abc123")
driver.find_element_by_xpath('//input[@name="cnfpassword"]').send_keys("abc123")
driver.find_element_by_xpath('//input[@name="first_name"]').send_keys("Nilanjana")
driver.find_element_by_xpath('//input[@name="last_name"]').send_keys("Bala")
driver.find_element_by_xpath('//input[@value= "female"]').click()
driver.find_element_by_xpath('//input[@name="reading"]').click()
driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("Nilanjana")
driver.find_element_by_xpath('//textarea[@id="textarea"]').send_keys("abc")
driver.find_element_by_xpath('//input[@id="agree"]').click()
driver.find_element_by_xpath('//button[@id="submitForm"]').click()






