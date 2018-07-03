'''coded by http://dragoon.ooo'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\\Asus\\Desktop\\Py\\AutoSteamAccountCreator\\chromedriver.exe")

driver.get("https://temp-mail.org/en/") #0
email = driver.find_element_by_id("click-to-copy")
email.click()

driver.execute_script("window.open('');") #1
driver.switch_to_window(driver.window_handles[1])
driver.get("https://store.steampowered.com/join")
e = driver.find_element_by_id("email")
e.send_keys(Keys.CONTROL, 'v')
ee = driver.find_element_by_id("reenter_email")
ee.send_keys(Keys.CONTROL, 'v')
i = driver.find_element_by_id("captchaImg")
print(i.get_attribute('src'))
ii = raw_input("Solve The Capcha: ")
iit = driver.find_element_by_id("captcha_text")
iit.send_keys(ii)
agree = driver.find_element_by_id('i_agree_check')
agree.click()
con = driver.find_element_by_id('createAccountButton')
con.click()


driver.switch_to_window(driver.window_handles[0])
driver.get("https://temp-mail.org/en/")
driver.implicitly_wait(10)
inbox = driver.find_element_by_class_name("title-subject")
inbox.click()
inbo = driver.find_element_by_xpath("//span[@style='border-radius: 2px;display: block;padding: 0;font-size: 20px;line-height: 32px']")
inbo.click()
#class title-subject
#class glyphicon glyphicon-chevron-right
#path //span[@style='border-radius: 2px;display: block;padding: 0;font-size: 20px;line-height: 32px']
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

# id accountname
#password
#reenter_password
#//span[contains(text(),'Complete Sign-up')]
driver.execute_script("window.open('');") #2
driver.switch_to_window(driver.window_handles[2])
driver.get('https://www.dashlane.com/features/password-generator')
u = driver.find_element_by_class_name("element white js-copy-password-btn green")
u.click()
driver.switch_to_window(driver.window_handles[0])

uu = driver.find_element_by_id("accountname")
uu.send_keys(Keys.CONTROL, 'v')

driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[3]) #3
driver.get('https://textuploader.com')
ID = driver.find_element_by_id("textdata")
ID.send_keys("Username: ")
ID.send_keys(Keys.CONTROL, 'v')
ID.send_keys("                                                                                                                      ")

driver.switch_to_window(driver.window_handles[2])
driver.get('https://www.dashlane.com/features/password-generator')
p = driver.find_element_by_class_name("element white js-copy-password-btn green")
p.click()

driver.switch_to_window(driver.window_handles[0])
pp = driver.find_element_by_id("password")
pp.send_keys(Keys.CONTROL, 'v')

rpp = driver.find_element_by_id("reenter_password")
rpp.send_keys(Keys.CONTROL, 'v')

complete = driver.find_elements_by_xpath("//span[contains(text(),'Complete Sign-up')]")

driver.switch_to_window(driver.window_handles[3])
ID.send_keys("Password: ")
ID.send_keys(Keys.CONTROL, 'v')

link = driver.current_url
print(link)
