'''
Created on Dec 1, 2015

@author: van.ngo
'''

class LoginPage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.txtUsername = "//input[@id='mod-login-username']"
        self.txtPassword = "//input[@id='mod-login-password']"
        self.btnLogin = "//div[@class = 'button-holder']//a"