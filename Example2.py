'''
Created on Nov 25, 2015

@author: van.ngo
'''
from datetime import date
from time import strftime, gmtime, localtime
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


joomlaurl = "http://192.168.189.207/joomla/administrator/index.php"
username = "admin"
password = "admin"
usernametextxpath = "//input[@id='mod-login-username']"
passwordtextxpath = "//input[@id='mod-login-password']"
loginbuttonxpath = "//div[@class = 'button-holder']//a"
contentelementxpath = "//div[@id = 'module-menu']//a[text() = 'Content']"
acticleelementxpath = "//div[@id = 'module-menu']//a[text() = 'Article Manager']"
newbuttonxpath = "//div[@id = 'toolbar']//li[@id = 'toolbar-new']/a"
titlefieldxpath = "//ul[@class = 'adminformlist']//input[@class= 'inputbox required']"
title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
print(title)