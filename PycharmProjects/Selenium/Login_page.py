import time

from selenium import webdriver

def login():
    driver = webdriver.Chrome("/Users/nilanjana/SourceCode/Python/browser_driver/mac/chromedriver")
    driver.get("http://mytestinglabs.in/")
    driver.find_element_by_name("email").send_keys("nilanjanabala14@gmail.com")
    driver.find_element_by_id("sign-in").click()
    time.sleep(5)
    return driver