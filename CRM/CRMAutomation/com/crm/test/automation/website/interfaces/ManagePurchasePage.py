# coding=utf-8
'''
Created on Sep 23, 2015

@author: phuong.dang
'''

class ManagePurchasePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.pagUnique = "//title[contains(. ,'Purchase Request - CRM')]"
        
        self.btnAddNew = "//button[@class = 'button addnew']"
        self.btnDelete = "//button[@class = 'button delete']"
        self.cbxRole = "//select[@id = 'Role']"
        
        self.txtPurchaseRequestKeyWord = "//input[@id = 'txtKeyword']"
        self.btnFilter = "//button[@class = 'button filter']"
        self.celPurchaseRequest = "//table[contains(@class ,'btable')]//td[descendant::a[text() = '$Purchase_Request_ID$']]"
        self.btnEditByPurchaseRequestID = "//table[contains(@class ,'btable')]//tr[descendant::a[text() = '$Purchase_Request_ID$']]//input[@class = 'icon edit']"
        self.lnkPurchaseRequestID = "//table[contains(@class ,'btable')]//a[text() = '$Purchase_Request_ID$']"
        self.chxSelectPurchaseRequest = "//tr[contains(@class, 'ui-widget-content') and descendant::a[text() = '$Purchase_Request_ID$']]//input[@class = 'cbox']"
        
        self.btnOK = "//div[@class = 'pbox']//button[@class = 'button ok']"
        self.msgDeleteSuccessfully = "//div[@class = 'msgSuccess' and contains(text(), '1 purchase request(s) has been deleted successfully')]"
        self.tblPurchaseRequest = "//table[contains(@class, 'btable')]"