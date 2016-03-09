# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''
import os
import unittest

from com.crm.test.automation.website.actions.Common import generateUniqueValue, \
    logWarning
from com.crm.test.automation.website.actions.pages.CRMFactoryPage import CRMFactoryPage
from com.crm.test.automation.website.module.Config import Config


class CRMAbstractTest(Config):
    
    def __init__(self):
        Config.__init__(self)
        
        # Set current path to environment
#         os.environ['ANKI_PATH'] = (os.path.dirname(os.path.realpath(__file__)))
         
        os.environ['ANKI_ERRORS'] = "0"
        os.environ['ANKI_WARNINGS'] = "0"

        # Load interface elements and private functions for Login page
        self.loginPage = CRMFactoryPage.getLoginPage()
        
        # Load interface elements and private functions for Home page
        self.homePage = CRMFactoryPage.getHomePage()
        
        # Load interface elements and private functions for Manage Purchase page
        self.managePurchasePage = CRMFactoryPage.getManagePurchasePage()
       
        # Load interface elements and private functions for Header Section
        self.header = CRMFactoryPage.getHeaderSection()
        
        # Load interface elements and private functions for AddNewPurchaseRequest page
        self.addNewPurchaseRequestPage = CRMFactoryPage.getAddNewPurchaseRequest()
        
        # Load interface elements and private functions for EditPurchaseRequest page
        self.editPurchaseRequestPage = CRMFactoryPage.getEditPurchaseRequest()
      
        # Load interface elements and private functions for PurchaseRequestDetails page
        self.purchaseRequestDetails = CRMFactoryPage.getPurchaseRequestDetails()
       
    def generateLogFilePath(self):
        try:
            logFileName = unittest.TestCase.id(self)
            logFileName = str(logFileName).split(".")[str(logFileName).count(".")-1] + "." + str(logFileName).split(".")[str(logFileName).count(".")]
            logFileName = logFileName.replace("__main__.", "")
            logFileName = logFileName.replace(".", "-")
            logFileName = logFileName + "-" + generateUniqueValue() + ".log"
             
            # Process to calculate the length of log file name
            if len(logFileName) > 124:
                logFileName = "..." + str(logFileName)[-121:]
                 
            # Set current path to environment
#             os.environ['ANKI_LOG_PATH'] = str(os.environ['ANKI_PATH']).replace("\\", "/") + "/../../../../../../_logs/" + logFileName
             
        except Exception, e:
            logWarning(str(e))