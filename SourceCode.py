#coded by http://dragoon.ooo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Arsh\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://temp-mail.org/en/")
email = driver.find_element_by_id("click-to-copy")
email.click()

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

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.get('https://temp-mail.org/en/')
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
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.get('https://www.dashlane.com/features/password-generator')
u = driver.find_element_by_class_name("element white js-copy-password-btn green")
u.click()
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

uu = driver.find_element_by_id("accountname")
uu.send_keys(Keys.CONTROL, 'v')

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.get('https://www.dashlane.com/features/password-generator')
p = driver.find_element_by_class_name("element white js-copy-password-btn green")
p.click()
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

pp = driver.find_element_by_id("password")
pp.send_keys(Keys.CONTROL, 'v')

rpp = driver.find_element_by_id("reenter_password")
rpp.send_keys(Keys.CONTROL, 'v')

complete = driver.find_elements_by_xpath("//span[contains(text(),'Complete Sign-up')]")
