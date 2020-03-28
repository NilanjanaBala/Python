import time
from Login_page import login

driver = login()
driver.find_element_by_link_text("Switch To").click()
driver.find_element_by_link_text("Windows").click()
driver.find_element_by_link_text("Open in new tab").click()
driver.find_element_by_id("buttonOne").click()
print(driver.title)
active_window = driver.current_window_handle
windows = driver.window_handles
print(windows)
for current_window in windows:
    print(current_window)
    driver.switch_to.window(current_window)
    time.sleep(3)
    print(driver.title)
    if 'JobsRally' in driver.title:
        print("i am going to close the window name: ", driver.title)
        driver.close()
    else:
        print("My page name is : ", driver.title)
# driver.switch_to.window(active_window)