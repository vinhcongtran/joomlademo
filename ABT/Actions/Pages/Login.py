'''
Created on Dec 1, 2015

@author: van.ngo
'''
import time

from selenium import webdriver

from ABT.Interfaces.LoginPage import LoginPage


class Login(LoginPage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        LoginPage.__init__(self)

    ##############################################################################################################
    # Open new browser
    # @param driver: type of browser 
    # @return browser object
    ##############################################################################################################    
    def openBrowser(self):
        driver = webdriver.Firefox()
        time.sleep(5)
        return driver


    ##############################################################################################################
    # Navigate to a url
    # @param driver: type of browser 
    # @param url: the url expected to navigate
    ##############################################################################################################    
    def navigate(self, driver, url):
        driver.get(url)
        
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
        
        