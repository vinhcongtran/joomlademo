'''
Created on Sep 25, 2015

@author: phuong.dang
'''

import unittest

from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.CRMAbstractTest import CRMAbstractTest

class BasePurchaseTestCase(unittest.TestCase, CRMAbstractTest):
    
    def setUp(self):
        CRMAbstractTest.__init__(self)
        
        # Navigate to Login page
        self.loginPage.navigateToWeb(self.cfCrmUrl, self.cfDriver)
        
        logInfo("Login with a requestor account")
        self.loginPage.loginCRM(self.cfRequestorUserName, self.cfRequestorPassword)
        
        logInfo("Click Purchase Request thumbmail on Home page")
        self.homePage.clickThumbnail(self.cfThumbnailPurchaseRequest)
         
        logInfo("Click 'Add New' button on Manage Purchase page")
        self.managePurchasePage.clickAddNewButton()
        
        logInfo(" Enter all required fields with valid data")
        self.addNewPurchaseRequestPage.enterPurchaseRequestInfo(requestType = self.cfRequestTypeEquipment, department = self.cfDepartmentBOM, expectedDate = self.cfExpectedDate, 
                                                                justification = self.cfJustification, billableToClient = self.cfBillableToClientNo, description = self.cfDescription, 
                                                                paymentMethod = self.cfPaymentMethodCash, moneyType = self.cfMoneyTypeUSD, salesTax = self.cfSalesTaxNoSalesTax,
                                                                resolution = self.cfResolutionNew, forwardTo = self.cfForwardTo)
        
        
        
        logInfo("Click Save button")
        self.addNewPurchaseRequestPage.clickSaveButton()

