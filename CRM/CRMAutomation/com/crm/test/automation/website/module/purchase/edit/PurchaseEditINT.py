# coding=utf-8
'''
Created on March 7, 2016


TC03 - User is able to open Edit Purchase Request page from Manage request page or form Detail Purchase page

@author: van.ngo
'''
import os
import unittest

from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.purchase.BasePurchaseTestCase import BasePurchaseTestCase


class PurchaseEditINT(BasePurchaseTestCase):
    global glPurchaseRequestID 
    def TC_03(self):
        logInfo("TC03 - User is able to open Edit Purchase Request page from Manage request page or form Detail Purchase page")   
        
        #Pre-condition: Login with a valid account and have at least one new purchase request created
        purchaseRequestID = self.managePurchasePage.getPurchaseRequestID()
        
        logInfo("Step 1 - Click on  Edit Purchase Request button from Manage request page")
        self.managePurchasePage.clickEditPurchaseRequestButton(purchaseRequestID = purchaseRequestID)
        
        logInfo("VP - User is able to open Edit Purchase Request page from Manage request page")
        self.editPurchaseRequestPage.checkTheCorrespondingEditPurchasePageIsDisplayed()
        
        logInfo("Step 2 - Hit Cancel button to go back to Manage Request page")
        self.editPurchaseRequestPage.clickCancelButton()
        
        logInfo("Step 3 - Click on Purchase Request ID from Manage request page")
        self.managePurchasePage.clickPurchaseRequestByID(purchaseRequestID = purchaseRequestID)
        
        logInfo("Step 4 - Click Edit button on Purchase Request Details")
        self.purchaseRequestDetails.clickEditButton()
        
        logInfo("VP - User is able to open Edit Purchase Request page from Manage request page")
        self.editPurchaseRequestPage.checkTheCorrespondingEditPurchasePageIsDisplayed()
        
        PurchaseEditINT.glPurchaseRequestID = purchaseRequestID
        
    def tearDown(self):
        logInfo("Go to Manage request page")
        self.editPurchaseRequestPage.navigateToWeb(self.cfManagePurchaseRequestUrl, self.cfDriver)
        
        logInfo("Delete the created purchase request")
        self.managePurchasePage.deleteAPurchaseRequestByID(purchaseRequestID = PurchaseEditINT.glPurchaseRequestID)
        
        logInfo("Log out of the system")
        self.header.logOut()
        
        self.loginPage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))

if __name__ == '__main__':
    
    testcaseName = "TC_03"
    
    suite = unittest.TestSuite()
    suite.addTest(PurchaseEditINT(testcaseName))
    runner = unittest.TextTestRunner()
    runner.run(suite)
