'''
Created on Nov 19, 2015

TC04 - Delete button is only available with Requestor role
TC05 - User can delete a purchase request

@author: vinh.tran
'''
import os
import unittest

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.purchase.BasePurchaseTestCase import BasePurchaseTestCase


class PurchaseDeleteINT(BasePurchaseTestCase):
    global glPurchaseRequestID
    def TC_04(self):
        logInfo("TC04 - Delete button is only available with Requestor role")   
        #Pre-condition: Login with a requestor account
        purchaseRequestID = self.managePurchasePage.getPurchaseRequestID()
        
        logInfo("Step 1 - Search for a purchase request")
        self.managePurchasePage.filterPurchaseRequestByID(purchaseRequestID = purchaseRequestID)
        
        logInfo("VP - Delete button display")
        self.managePurchasePage.checkDeleteButtonDisplayed()
        
        logInfo("Step 2 - Switch to Department Head role")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsDepartmentHead)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()
        
        logInfo("Step 3 - Switch to Purchasing role")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsPurchasing)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()

        logInfo("Step 4 - Switch to Director of Global Operations role")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsDirectorOfGlobalOperations)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()

        logInfo("Step 5 - Switch to VP of Sales")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsVPOfSales)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()
        
        logInfo("Step 6 - Switch to President/CEO")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsPresidentCEO)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()
        
        logInfo("Step 7 - Switch to US Accounting")
        self.managePurchasePage.switchRoleByRoleName(roleName = self.cfLoginAsUSAccounting)
        
        logInfo("VP - Delete button DOES NOT display")
        self.managePurchasePage.checkDeleteButtonDoesNotDisplay()
        
        PurchaseDeleteINT.glPurchaseRequestID = purchaseRequestID
        
    def TC_05(self):
        logInfo("TC05 - User can delete a purchase request")   
        
        #Pre-condition: Login with a valid account and have at least one new purchase request created 
        purchaseRequestID = self.managePurchasePage.getPurchaseRequestID()

        logInfo("Step 1 - Delete a purchase request")
        self.managePurchasePage.deleteAPurchaseRequestByID(purchaseRequestID = purchaseRequestID)
        
        logInfo("VP - the purchase request is deleted")
        self.managePurchasePage.checkAPurchaseRequestIsDeleted(purchaseRequestID)
        PurchaseDeleteINT.glPurchaseRequestID = purchaseRequestID
        
    def tearDown(self):
        logInfo("Delete the created purchase request")
        self.managePurchasePage.deleteAPurchaseRequestByID(purchaseRequestID = PurchaseDeleteINT.glPurchaseRequestID)
        
        logInfo("Log out of the system")
        self.header.logOut()
        
        self.loginPage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))
          
if __name__ == '__main__':
    
    testcaseName = "test_c23401"
    
    # If the test case name is not null, then run only this test case 
    if testcaseName != "":
        suite = unittest.TestSuite()
        suite.addTest(PurchaseDeleteINT(testcaseName))
        runner = unittest.TextTestRunner()
        runner.run(suite)
    else:
        if is_running_under_teamcity():
            runner = TeamcityTestRunner()
        else:
            runner = unittest.TextTestRunner()
        unittest.main(testRunner=runner)