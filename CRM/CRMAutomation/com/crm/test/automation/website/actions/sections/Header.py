# coding=utf-8
'''
Created on Sep 18, 2015

@author: phuong.dang
'''
# from xlwt.antlr import ifelse

from selenium.webdriver.common.action_chains import ActionChains

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, wait
from com.crm.test.automation.website.interfaces.HeaderSection import HeaderSection
from com.crm.test.automation.website.actions.pages.Login import Login
from com.crm.test.automation.website.interfaces.LoginPage import LoginPage


class Header(AbstractPage, HeaderSection):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        HeaderSection.__init__(self)
    
    ##############################################################################################################
    # Navigate to a page by clicking on a menu item
    # @param driver: type of browser
    # @param path: path of menu item, menu items separates to each other by '>' (e.g.: Content>Article Manager)
    ##############################################################################################################       
    def navigateMenu(self, path):
        i = 0
        n = path.count(">")
        while n > i:
            x = path.find(">")
            e = path[:x]
            self.moveToElement("//a[text() ='" + e + "']")
            path = path[x+1:]
            i +=1
            if i == n:
                self.click("//a[text() ='" + e + "']")
                
    def logOut(self):
        self.click(self.lnkLogout)
        if self.doesElementExisted(LoginPage().pagUnique) == True:
            logInfo("Log out of system successfully")
        else:
            logWarning("Log out unsuccessfully")