# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.pages.AddNewPurchaseRequest import AddNewPurchaseRequest
from com.crm.test.automation.website.actions.pages.EditPurchaseRequest import EditPurchaseRequest
from com.crm.test.automation.website.actions.pages.Home import Home
from com.crm.test.automation.website.actions.pages.Login import Login
from com.crm.test.automation.website.actions.pages.ManagePurchase import ManagePurchase
from com.crm.test.automation.website.actions.pages.PurchaseRequestDetails import PurchaseRequestDetails
from com.crm.test.automation.website.actions.sections.Header import Header


class CRMFactoryPage(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    ''' Factory methods to create page objects
    '''
    
    @staticmethod
    def getLoginPage():
        return Login()
    
    @staticmethod
    def getHomePage():
        return Home()
    
    @staticmethod
    def getManagePurchasePage():
        return ManagePurchase()
    
    @staticmethod
    def getHeaderSection():
        return Header()
    
    @staticmethod
    def getAddNewPurchaseRequest():
        return AddNewPurchaseRequest()
    
    @staticmethod
    def getEditPurchaseRequest():
        return EditPurchaseRequest()
    
    @staticmethod
    def getPurchaseRequestDetails():
        return PurchaseRequestDetails()