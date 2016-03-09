'''
Created on Sep 25, 2015

@author: phuong.dang
'''
import os
import unittest

from com.crm.test.automation.website.module.CRMAbstractTest import CRMAbstractTest

class BasePurchaseGeneralTestCase(unittest.TestCase, CRMAbstractTest):
    
    def setUp(self):
        CRMAbstractTest.__init__(self)
        
        # Navigate to Login page
        self.loginPage.navigateToWeb(self.cfCrmUrl, self.cfDriver)
    
    def tearDown(self):

        self.loginPage.closeBrowser()
        self.assertEqual(int(os.environ['ANKI_WARNINGS']), int(os.environ['ANKI_ERRORS']))