from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Asus\\Desktop\\Py\\AutoSteamAccountCreator\\chromedriver.exe")
driver.get("http://www.google.com/")

#open tab
driver.execute_script("window.open('');")

# Load a page
driver.switch_to_window(driver.window_handles[1])
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
