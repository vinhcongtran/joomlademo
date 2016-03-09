# coding=utf-8
'''
Created on Sep 23, 2015

@author: phuong.dang
'''

class LoginPage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.pagUnique = "//title[text() = 'CRM - Login']"
        
        self.txtUsername = "//input[@name = 'username']"
        self.txtPassword = "//input[@name = 'password']"
        self.btnLogin = "//input[@class = 'btn_lg']"