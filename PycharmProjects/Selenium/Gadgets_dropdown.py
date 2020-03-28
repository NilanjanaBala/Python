import time
from selenium.webdriver.support.ui import Select

from Login_page import login

driver = login()
driver.find_element_by_xpath("//span[text()='Gadgets']").click()
driver.find_element_by_xpath('//a[contains(@href,"dropdown")]').click()

dropdown= driver.find_element_by_xpath('//select[@name="country"]')
select = Select(dropdown)
select.select_by_index(3)
time.sleep(4)
select.select_by_value("IN")
time.sleep(3)
select.select_by_visible_text("Australia")
time.sleep(2)

dropdown_multi = driver.find_element_by_xpath('//select[@id="multiSelect"]')
select = Select(dropdown_multi)
select.select_by_value("AS")
time.sleep(2)
select.select_by_index(2)
time.sleep(3)
select.select_by_visible_text("Angola")
select.select_by_value("IN")
time.sleep(5)
select.deselect_by_visible_text("Albania")
select.deselect_by_index(6)
select.deselect_by_value("AS")
# print(select.first_selected_option.text)
# all_selected_options = select.all_selected_options
# print(all_selected_options)
# select.deselect_all()
#
# for current_option in all_selected_options:
#     print(current_option.text)
