import time
from Login_page import login
from PycharmProjects.Selenium.alerts_function import *

def frames():
    driver.switch_to.frame('frameW3C')
    driver.switch_to.frame('frameW3C')

driver.find_element_by_link_text("Switch To").click()
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("Single iframe").click()
time.sleep(2)
driver.switch_to.frame('frameJR')
alert_ok()
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_xpath('//a[@href="#multipleFrames"]').click()
time.sleep(2)
frames()
time.sleep(1)
alert_ok()
alert_two_buttons()
alert_three_buttons()
