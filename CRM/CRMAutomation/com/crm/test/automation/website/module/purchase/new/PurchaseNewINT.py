# coding=utf-8
'''
Created on March 7, 2016


TC02 - User is able to add new Purchase Request when saving with required fields are filled

@author: van.ngo
'''
import unittest
import os
from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.purchase.general.BasePurchaseGeneralTestCase import BasePurchaseGeneralTestCase


class PurchaseNewINT(BasePurchaseGeneralTestCase ):
    def TC_02(self):
        logInfo("TC02 - User is able to add new Purchase Request when saving with required fields are filled")   

        #Pre-condition: Login with a valid account and have at least one new purchase request created 
        self.loginPage.loginCRM(self.cfRequestorUserName, self.cfRequestorPassword)
        
        logInfo("Step 1 - Click Purchase Request thumbmail on Home page")
        self.homePage.clickThumbnail(self.cfThumbnailPurchaseRequest)
         
        logInfo("Step 2 - Click 'Add New' button on Manage Purchase page")
        self.managePurchasePage.clickAddNewButton()
        
        logInfo("Step 3 - Enter all required fields with valid data")
        self.addNewPurchaseRequestPage.enterPurchaseRequestInfo(requestType = self.cfRequestTypeEquipment, department = self.cfDepartmentBOM, expectedDate = self.cfExpectedDate, 
                                                                justification = self.cfJustification, billableToClient = self.cfBillableToClientNo, description = self.cfDescription, 
                                                                paymentMethod = self.cfPaymentMethodCash, moneyType = self.cfMoneyTypeUSD, salesTax = self.cfSalesTaxNoSalesTax,
                                                                resolution = self.cfResolutionNew, forwardTo = self.cfForwardTo)
        
        
        logInfo("Step 4 - Click Save button")
        self.addNewPurchaseRequestPage.clickSaveButton()
        
        logInfo("VP - User is able to add new Purchase Request")
        self.addNewPurchaseRequestPage.checkAddANewPurchaseSuccessfully()
        
    def tearDown(self):
        logInfo("Delete the created purchase request")
        self.managePurchasePage.deleteAPurchaseRequestByID(purchaseRequestID = self.managePurchasePage.getPurchaseRequestID())
        
        logInfo("Log out of the system")
        self.header.logOut()
        
        self.loginPage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))
        
if __name__ == '__main__':
    
    testcaseName = "TC_02"
    
    suite = unittest.TestSuite()
    suite.addTest(PurchaseNewINT(testcaseName))
    runner = unittest.TextTestRunner()
    runner.run(suite)
