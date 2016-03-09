# coding=utf-8
'''
Created on March 7, 2016

TC01 - User is able to access Manage Request from Request header menu or Purchase Request thumbnail on Home page

@author: van.ngo
'''
import unittest


from com.crm.test.automation.website.actions.Common import logInfo
from com.crm.test.automation.website.module.purchase.general.BasePurchaseGeneralTestCase  import BasePurchaseGeneralTestCase 


class PurchaseGeneralINT(BasePurchaseGeneralTestCase ):

    def TC_01(self):
        logInfo("TC01 - User is able to access Manage Request from Request header menu or Purchase Request thumbnail on Home page")   
        #Pre-condition : Login with a valid account
        logInfo("Login with a valid account")
        self.loginPage.loginCRM(self.cfRequestorUserName, self.cfRequestorPassword)
        
        logInfo("Step 1 - Click Purchase Request thumbmail on Home page")
        self.homePage.clickThumbnail(self.cfThumbnailPurchaseRequest)
         
        logInfo("VP - User is able to access Manage Request")
        self.managePurchasePage.checkTheCorrespondingManagePurchasePageIsDisplayed()

        logInfo("Step 2 - Navigate to Request> Purchase Request> Manage Request")
        self.header.navigateMenu("Requests>Purchase Request>Manage Request")
        
        logInfo("VP - User is able to access Manage Request")
        self.managePurchasePage.checkTheCorrespondingManagePurchasePageIsDisplayed()
        

if __name__ == '__main__':
    
    testcaseName = "TC_01"
    
    suite = unittest.TestSuite()
    suite.addTest(PurchaseGeneralINT(testcaseName))
    runner = unittest.TextTestRunner()
    runner.run(suite)
