'''
Created on Dec 1, 2015

@author: van.ngo
'''

from time import localtime, strftime
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from ABT.Interfaces.CommonUI import CommonUI
from ABT.Modules.Common.Config import Config
import time




class CommonActions(CommonUI,Config):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.username = "admin"
        self.password = "admin"
        self.joomlaUrl = "http://192.168.189.207/joomla/administrator/index.php"
        CommonUI.__init__(self)
        Config.__init__(self)
        
    def logInfo(self, log):
        print strftime("%Y-%m-%d %H:%M:%S: ", localtime()) + log
    
    def wait(self, seconds):
        time.sleep(seconds)
        
    def logOut(self, driver):
        try:
            driver.find_element_by_xpath(self.lnkLogOut).click()
        except:
            print ("Please log in before logging out")
            
    def openBrowser(self):
        try:
            driver = webdriver.Firefox()
            self.logInfo("Open browser successfully")
            driver.maximize_window()
            driver.set_page_load_timeout(self.cfTimeWait)
            return driver
        except Exception, e:
            print str(e) 
            self.logInfo("Open browser unsuccessfully")
            
    ##############################################################################################################
    # Navigate to a url
    # @param driver: type of browser 
    # @param url: the url expected to navigate
    ##############################################################################################################    
    def navigate(self, driver, url):
        try:
            driver.implicitly_wait(self.cfTimeWait)
            driver.get(url)
            self.logInfo("Navigate to %s successfully" % url)
            return driver
        except Exception, e:
            print str(e)
            self.logInfo("Navigate to %s unsuccessfully" % url)
    
    def verifyTrue(self, expression, passMsg, failMsg):
        try:
            if expression == True:
                self.logInfo(passMsg)
 
#                 unittest.TestCase.assertTrue(expression, failMsg)
            unittest.TestCase.assertTrue(self, expression, failMsg)

        except AssertionError, e:
            self.logInfo(str(e))
            
    
    def doesElementDisplay(self, driver, xPathElement):
        try:
            element = self.getElementByXPath(driver, xPathElement)
            status = element.is_displayed()
            return status
        except Exception, e:
            self.logInfo(str(e))
        return None
        
    def getElementByXPath(self, driver,  xPath):
        element = None
        try:
            element = driver.find_element_by_xpath(xPath)
            return element
        except Exception, e:
            print e
            self.logInfo("Cannot get element with xpath: " + xPath)
        return None
    
    def doesElementNotExisted(self,driver, xPath, timeout = 5):
        try:
            WebDriverWait(driver, timeout).until_not(driver.find_element_by_xpath(xPath))
            return True
        except Exception:
            return False
            
                
    def switchToFrame(self, driver, frameReference):
        try:
            driver.switch_to_frame(frameReference)
        except Exception, e:
            print e
            self.logInfo("Cannot switch to frame " + frameReference) 
            
    def switchToLatestWindow(self, driver):
        self.wait(1)
        if driver != None:
            driver.switch_to_window(self.Browser().window_handles[-1]) 
   
    