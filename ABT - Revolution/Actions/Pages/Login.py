'''
Created on Dec 1, 2015

@author: van.ngo
'''

from ABT.Interfaces.LoginPage import LoginPage
from ABT.Modules.Common.Config import Config


class Login(LoginPage, Config):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        LoginPage.__init__(self)
        Config.__init__(self)

   
        
    def enterUsername(self, driver, username):
        driver.find_element_by_xpath(self.txtUsername).send_keys(username)
    
    def enterPassword(self, driver, password):
        driver.find_element_by_xpath(self.txtPassword).send_keys(password)
    
    def clickLoginButton(self, driver):
        driver.find_element_by_xpath(self.btnLogin).click()
     
    ##############################################################################################################
    # Log into an existing account
    # @param driver: type of browser 
    # @param username, password: the username and password expected to log
    ##############################################################################################################       
    def login(self, driver, username, password):
        self.enterUsername(driver, username)
        self.enterPassword(driver, password)
        self.clickLoginButton(driver)
        
        