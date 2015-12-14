'''
Created on Dec 12, 2015

@author: vinh.cong.tran
'''
import unittest

from selenium import webdriver

from ABT.Modules.Common.Config import Config


class AbstractPage(unittest.TestCase, Config):
    browser = None
    
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        Config.__init__(self)
        
    def Browser(self):
        return self.browser
    
    def openBrowser(self):
        try:
            driver = webdriver.Firefox()
            self.logInfo("==========Open browser successfully, Begin running ===============")
            driver.maximize_window()
            driver.set_page_load_timeout(self.cfTimeWait)
            return driver
        except Exception, e:
            print str(e) 
            self.logInfo("\nOpen browser unsuccessfully")
            
    ##############################################################################################################
    # Close browser
    # @param none 
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################             
    def closeBrowser(self):
        try:
            AbstractPage.Browser().quit()
            AbstractPage.browser = None
            self.logInfo("Browser is closed")
        except Exception:
            self.logWarning("Browser isn't closed")