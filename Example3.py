'''
Created on Nov 30, 2015

@author: van.ngo
'''
from datetime import date
from time import strftime, localtime
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


joomlaurl = "http://192.168.189.207/joomla/administrator/index.php"
username = "admin"
password = "admin"
articletext = "This is an article"
usernametextxpath = "//input[@id='mod-login-username']"
passwordtextxpath = "//input[@id='mod-login-password']"
loginbuttonxpath = "//div[@class = 'button-holder']//a"
contentelementxpath = "//div[@id = 'module-menu']//a[text() = 'Content']"
acticleelementxpath = "//div[@id = 'module-menu']//a[text() = 'Article Manager']"
newbuttonxpath = "//div[@id = 'toolbar']//li[@id = 'toolbar-new']/a"
titlefieldxpath = "//ul[@class = 'adminformlist']//input[@class= 'inputbox required']"
title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
categoryelementxpath = "//select[@name='jform[catid]']/option[contains(.,'Extensions')]"
textarexpath = "html/body"
saveandclosexpath = "//div[@id = 'toolbar']//li[@id = 'toolbar-save']/a"



#Step 1: Navigate to Joomla administrator admin page
driver = webdriver.Firefox()
time.sleep(8)
driver.get(joomlaurl)

#Step 2: Enter valid username into Username field
driver.find_element_by_xpath(usernametextxpath).send_keys(username) #put your actual username
 
#Step 3: Enter valid password into Password field
driver.find_element_by_xpath(passwordtextxpath).send_keys(password) 
 
#Step 4: Click on 'Log in' button
driver.find_element_by_xpath(loginbuttonxpath).click()

#Step 5: Select Content > Article Manager
contentelement = driver.find_element_by_xpath(contentelementxpath)
ActionChains(driver).move_to_element(contentelement).perform()

acticleelement = driver.find_element_by_xpath(acticleelementxpath)
ActionChains(driver).move_to_element(acticleelement).perform()
acticleelement.click()


#Step 6: Click on 'New' icon of the top right toolbar
driver.find_element_by_xpath(newbuttonxpath).click()

#Step 7: Enter a title on 'Title' field
driver.find_element_by_xpath(titlefieldxpath).send_keys(title)

#Step 8: Select an item from the 'Category' dropdown list
driver.find_element_by_xpath(categoryelementxpath).click()

#Step 9: Enter value on 'Article Text' text area
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath(textarexpath).send_keys(articletext)
driver.switch_to.default_content()

#Step 10: Click on 'Save & Close' icon of the top right toolbar
driver.find_element_by_xpath(saveandclosexpath).click()

#VP: 1. "Article successfully saved" message is displayed
#2. Created article is displayed on the articles table
time.sleep(2)

print("van ngo")
#  
# #Quitting the browser
# driver.quit()