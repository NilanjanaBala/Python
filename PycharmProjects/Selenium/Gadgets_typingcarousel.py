
from Login_page import login

driver = login()
driver.find_element_by_xpath("//span[text()='Gadgets']").click()
driver.find_element_by_xpath("//a[contains(@href, 'typingcarousel')]")
