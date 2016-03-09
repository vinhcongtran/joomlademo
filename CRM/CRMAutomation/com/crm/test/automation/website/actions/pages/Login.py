# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.LoginPage import LoginPage


class Login(AbstractPage, LoginPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        LoginPage.__init__(self)
        

    #####################
    # Other actions
    #####################
        
    def loginCRM(self, username , password):
        try:
            self.enterUsername(username)
            self.enterPassword(password)
            self.clickLoginButton()
            logInfo("Login successfully")
            
        except Exception, e:
            print str(e)
            logWarning("Login unsuccessfully, please check username and password" )
            # Close Browser and set test case is failed
            self.closeBrowser()
            self.fail()
    
    def enterPassword(self, password):
        self.enter(self.txtPassword, password)
    
    def enterUsername(self, username):
        self.enter(self.txtUsername, username)
        
    def clickLoginButton(self):
        self.click(self.btnLogin)