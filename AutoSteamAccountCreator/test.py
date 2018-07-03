from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Asus\\Desktop\\Py\\AutoSteamAccountCreator\\chromedriver.exe")

driver.get("https://www.bing.com")

driver.execute_script("window.open('http://dragoon.ooo', 'new window')")
driver.switch_to_window(driver.window_handles[1])
driver.get("http://google.com")
A = driver.find_element_by_id("lst-ib")
A.send_keys("xD")
driver.switch_to_window(driver.window_handles[0])
B = driver.find_element_by_id("sb_form_q")
B.send_keys("hehe")
a = 1
print (driver.current_url)
