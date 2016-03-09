# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''
import os

from com.crm.test.automation.website.actions.Common import getCurrentDateTime


verificationErrors = 0

class Config():
    def __init__(self):
        self.cfShortTime = 60
        self.cfImplicitlyTimeWait = 90
        self.cfPageLoadTimeout = 600
        self.cfDriver = os.environ.get('SELENIUM_DEVICE',"Firefox")
        self.cfCrmUrl = "http://192.168.190.92:8080/Authenticate/Index/?ReturnUrl=/"
        
        self.cfRequestorUserName = "trinh.kieu.nguyen"
        self.cfRequestorPassword = "1"
        self.cfManagePurchaseRequestUrl = "http://192.168.190.92:8080/PurchaseRequest"
        
        
        # Home Page
        self.cfThumbnailPurchaseRequest = "PurchaseRequest"
        
        #Add New Purchase request
        self.cfRequestTypeEquipment = "Equipment"
        self.cfExpectedDate = '20/Dec/2016'
        self.cfBillableToClientNo = "No"
        self.cfJustification = "This is for testing"
        self.cfDepartmentBOM = 'BOM'
        self.cfDescription = "This is description"
        self.cfPaymentMethodCash = 'Cash'
        self.cfMoneyTypeUSD = "USD"
        self.cfSalesTaxNoSalesTax = "No Sales Tax"
        self.cfResolutionNew = "New"
        self.cfForwardTo = "AldoK (Requestor)"
        
        # Manage Purchase Request
        self.cfLoginAsRequestor = "Requestor"
        self.cfLoginAsDepartmentHead = "Department Head"
        self.cfLoginAsPurchasing = "Purchasing"
        self.cfLoginAsDirectorOfGlobalOperations = "Director of Global Operations"
        self.cfLoginAsVPOfSales = "VP of Sales"   
        self.cfLoginAsPurchasing = "Purchasing"
        self.cfLoginAsPresidentCEO = "President/CEO"
        self.cfLoginAsUSAccounting = "US Accounting"       