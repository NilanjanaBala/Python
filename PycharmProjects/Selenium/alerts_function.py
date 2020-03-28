import time
from Login_page import login

driver = login()

def goto_alerts():
    driver.find_element_by_link_text("Switch To").click()
    driver.find_element_by_link_text("Alerts").click()

def alert_ok():
    driver.find_element_by_link_text("Alert with OK Button").click()
    driver.find_element_by_xpath("//button[@id='alertBtn']").click()
    driver.switch_to.alert.accept()
    time.sleep(3)

def alert_two_buttons():
    driver.find_element_by_link_text("Alert with OK and Cancel buttons").click()
    driver.find_element_by_xpath('//button[@onclick="alerttwo()"]').click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@onclick="alerttwo()"]').click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(3)

def alert_three_buttons():
    driver.find_element_by_link_text("Alert with Text box").click()
    driver.find_element_by_xpath('//button[@onclick="alertthree()"]').click()
    driver.switch_to.alert.send_keys("Nilanjana")
    driver.switch_to.alert.accept()

