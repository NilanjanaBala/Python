import time

from Login_page import login

driver = login()
click_gadgets = driver.find_element_by_xpath("//span[text()='Gadgets']")
click_gadgets.click()
driver.find_element_by_xpath('//a[contains(@href,"fileupload")]').click()
driver.find_element_by_xpath('//input[@type="file"]').send_keys("/Users/nilanjana/Desktop/download.png")
srcValue = driver.find_element_by_id("img-upload").get_attribute('src')
print(srcValue)

if "data:image" in srcValue:
    print("it is an image")
else:
    print("it is a document")




