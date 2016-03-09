# coding=utf-8
'''
Created on March 7, 2016
TC06 - User can filter only one purchase request with exactly matching ID

@author: van.ngo
'''
import os
import unittest

from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.purchase.BasePurchaseTestCase import BasePurchaseTestCase


class PurchaseFilterINT(BasePurchaseTestCase):
    
    global glPurchaseRequestID 
    
    def TC_06(self):
        logInfo("TC06 - User can filter only one purchase request with exactly matching ID")   
        
        #Pre-condition: Login with a valid account and have at least one new purchase request created
        purchaseRequestID = self.managePurchasePage.getPurchaseRequestID()

        logInfo("Step 1 - Filter the created purchase request")
        self.managePurchasePage.filterPurchaseRequestByID(purchaseRequestID = purchaseRequestID)
        
        logInfo("VP - User can filter only one purchase request with exactly matching ID")
        self.managePurchasePage.checkOnlyOnePurchaseRequestMarchingID(purchaseRequestID = purchaseRequestID)
        
        PurchaseFilterINT.glPurchaseRequestID = purchaseRequestID
        
    def tearDown(self):
        logInfo("Delete the created purchase request")
        self.managePurchasePage.deleteAPurchaseRequestByID(purchaseRequestID = PurchaseFilterINT.glPurchaseRequestID)
        
        logInfo("Log out of the system")
        self.header.logOut()
        
        self.loginPage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))

if __name__ == '__main__':
    
    testcaseName = "TC_06"
    
    suite = unittest.TestSuite()
    suite.addTest(PurchaseFilterINT(testcaseName))
    runner = unittest.TextTestRunner()
    runner.run(suite)
