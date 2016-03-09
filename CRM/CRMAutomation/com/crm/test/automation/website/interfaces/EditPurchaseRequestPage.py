# coding=utf-8
'''
Created on Sep 23, 2015

@author: phuong.dang
'''

class EditPurchaseRequestPage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.pagUnique = "//title[contains(text(), 'Edit Purchase Request')]"
        self.btnCancel = "//input[@class = 'cancel']"