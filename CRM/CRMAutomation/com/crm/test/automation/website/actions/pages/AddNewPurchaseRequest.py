# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.HomePage import HomePage
from com.crm.test.automation.website.interfaces.AddNewPurchaseRequestPage import AddNewPurchaseRequestPage
from com.crm.test.automation.website.actions.pages.ManagePurchase import ManagePurchase


class AddNewPurchaseRequest(AbstractPage, AddNewPurchaseRequestPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        AddNewPurchaseRequestPage.__init__(self)
        
    #####################
    # Check actions
    #####################        
    def checkAddANewPurchaseSuccessfully(self):
        msgAddNewSuccessfullExist = self.doesElementExisted(self.msgAddSuccessfully)
        purchaseRequestID = ManagePurchase().getPurchaseRequestID()
        purchaseRequestDisplayedInPurchaseTable = ManagePurchase().doesPurchaseRequestIDExist(purchaseRequestID)
        
        self.verifyTrue(msgAddNewSuccessfullExist == True and purchaseRequestDisplayedInPurchaseTable == True, "The purchase request " +purchaseRequestID + " is added successfully", "The purchase request " +purchaseRequestID + " is NOT added successfully")
    #####################
    # Click actions
    #####################
    def clickSaveButton(self):
        self.click(self.btnSave)

    #####################
    # Others actions
    #####################
    
    #expectedDate should be 'dd/mm/yy'
    def enterPurchaseRequestInfo(self, requestType, department, expectedDate, justification, billableToClient, description, paymentMethod , moneyType , salesTax , resolution , forwardTo ):
        self.selectExpectedDate(expectedDate)
        self.selectRequestType(requestType)
        self.selectDepartment(department)
        
        self.enterJustification(justification)
        
        self.selectBillableToClient(billableToClient)
        self.selectPaymentMethod(paymentMethod)
        self.selectMoneyType(moneyType)
        self.selectSalesTax(salesTax)
        self.selectResolution(resolution)
        self.selectForwardTo(forwardTo)
        
        self.enterDescription(description)
        
        
        
    def selectExpectedDate(self, expectedDate):
        self.click(self.btnDatePickerExpectedDate)
        
        #wait for date time picker display
        self.waitForElementExisted(self.pickerExpectedDate, 2000)
        
        #split expectedDate into Day, Month, Year
        x = expectedDate.find("/")
        day = expectedDate[:x]
        expectedDate = expectedDate[x+1:]
        x = expectedDate.find("/")
        month = expectedDate[:x]
        year = expectedDate[x+1:]
        
        self.selectExpectedMonth(month)
        #wait for date time picker loaded
        wait(1)
        self.selectExpectedYear(year)
        #wait for date time picker loaded
        wait(1)
        self.selectExpectedDay(day)

        
    def selectExpectedDay(self, day):
        element = self.lblExpectedDay.replace("$Expected_Day$", day)
        self.click(element)
        
    def selectExpectedMonth(self, month):
        self.selectItemByText(self.cbxExpectedMonth, month)
        
    def selectExpectedYear(self, year):
        self.selectItemByText(self.cbxExpectedYear, year)

    def selectRequestType(self, requestType):
        ele = self.getElementByXPath(self.cbxRequestType)
        self.selectItemByText(self.cbxRequestType, requestType) 
        
    def selectDepartment(self, department):
        self.selectItemByText(self.cbxDepartment, department)
        
    def enterJustification(self, justification):
        self.enter(self.taJustification, justification)
    
    def selectBillableToClient(self, billableToClient):
        element = self.rdbBillableToClient.replace("$Billable_To_Client$", billableToClient)
        self.click(element)

    def selectPaymentMethod(self, paymentMethod):
        element = self.rdbPaymentMethod.replace("$Payment_Method$", paymentMethod)
        self.click(element)
        
    def selectMoneyType(self, moneyType):
        element = self.rdbMoneyType.replace("$Money_Type$", moneyType)
        self.click(element)
        
    def selectSalesTax(self, salesTax):
        self.selectItemByText(self.cbxSalesTax, salesTax)
        
    def selectResolution(self, resolution):
        self.selectItemByText(self.cbxResolution, resolution)
        
    def selectForwardTo(self, forwardTo):
        self.selectItemByText(self.cbxForwardTo, forwardTo)
        
    def enterDescription(self, description):
        self.enter(self.txtDescription, description)
     
        