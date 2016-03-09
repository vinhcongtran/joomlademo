# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.ManagePurchasePage import ManagePurchasePage
from com.crm.test.automation.website.interfaces.AddNewPurchaseRequestPage import AddNewPurchaseRequestPage


class ManagePurchase(AbstractPage, ManagePurchasePage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        ManagePurchasePage.__init__(self)
        
    #####################
    # check actions
    #####################
        
    def checkTheCorrespondingManagePurchasePageIsDisplayed(self):
        titleExist = self.doesElementExisted(self.pagUnique)
        self.verifyTrue(titleExist == True, "The Manage Purchase page is displayed", "The Manage Purchase page is NOT displayed")
    
    def checkDeleteButtonDisplayed(self):
        self.verifyTrue(self.doesElementExisted(self.btnDelete) == True, "Delete button displays", "Delete button DOES NOT display")
    
    def checkDeleteButtonDoesNotDisplay(self):
        self.verifyTrue(self.doesElementExisted(self.btnDelete) == False, "Delete button DOES NOT display", "Delete button displays")
    
    def checkAPurchaseRequestIsDeleted(self, purchaseRequestID):
        msgDeleteSuccessfullyExist = self.doesElementDisplay(self.msgDeleteSuccessfully)
        purchaseRequestExist = self.doesPurchaseRequestIDExist(purchaseRequestID)
        
        self.verifyTrue(msgDeleteSuccessfullyExist == True and purchaseRequestExist == False, "The purchase request "+ purchaseRequestID + " is deleted", "The purchase request "+ purchaseRequestID + " is NOT deleted")
    
    def checkOnlyOnePurchaseRequestMarchingID(self, purchaseRequestID):
        tblPurchaseRequestRow = self.tblPurchaseRequest + "//tr[contains(@class, 'content')]"
        rowCount = len(AbstractPage.Browser().find_elements_by_xpath(tblPurchaseRequestRow))
        self.verifyTrue(rowCount == 1, "There is only one Purchase Request ID displaying", "There is NOTonly one Purchase Request ID displaying")

    #####################
    # click actions
    #####################
    def clickFilterButton(self):
        self.click(self.btnFilter)
        
    def clickAddNewButton(self):
        self.click(self.btnAddNew)
        
    def clickEditPurchaseRequestButton(self, purchaseRequestID):
        self.filterPurchaseRequestByID(purchaseRequestID)
        element = self.btnEditByPurchaseRequestID.replace("$Purchase_Request_ID$", purchaseRequestID)
        self.click(element)
        
    def clickPurchaseRequestByID(self,purchaseRequestID):
        self.filterPurchaseRequestByID(purchaseRequestID)
        element = self.lnkPurchaseRequestID.replace("$Purchase_Request_ID$", purchaseRequestID)
        self.click(element)
       
    def clickDeleteButton(self):
        self.click(self.btnDelete) 
        
    def clickOKButton(self):
        self.click(self.btnOK)
    #####################
    # Other actions
    #####################
    
    def getPurchaseRequestID(self):
        msgAddSuccessfull = self.getElementText(AddNewPurchaseRequestPage().msgAddSuccessfully)
        x = msgAddSuccessfull.find("'")
        temp = msgAddSuccessfull[x+1:]
        y = temp.find("'")
        purchaseRequestID = msgAddSuccessfull[x+1:x+y+1]
        return purchaseRequestID
    
    def doesPurchaseRequestIDExist(self, purchaseRequestID):
        self.filterPurchaseRequestByID(purchaseRequestID)
        purchaseRequestElement = self.celPurchaseRequest.replace("$Purchase_Request_ID$", purchaseRequestID)
        purchaseRequestExist = self.doesElementExisted(purchaseRequestElement)
        return purchaseRequestExist


    def filterPurchaseRequestByID(self, purchaseRequestID):
        try:
            self.enter(self.txtPurchaseRequestKeyWord, purchaseRequestID)
            self.clickFilterButton()
            #wait for searching
            wait(2)
        except Exception,e:
            print str(e)
            
    def switchRoleByRoleName(self, roleName):
        self.selectItemByText(self.cbxRole , roleName)
        
    def selectAPurchaseRequestByID(self,purchaseRequestID ):
        self.click(self.chxSelectPurchaseRequest.replace("$Purchase_Request_ID$", purchaseRequestID))
    
    def deleteAPurchaseRequestByID(self,purchaseRequestID):
        self.switchRoleByRoleName(self.cfLoginAsRequestor)
        purchaseRequestExist = self.doesPurchaseRequestIDExist(purchaseRequestID)
        if purchaseRequestExist == True:
            self.selectAPurchaseRequestByID(purchaseRequestID)
            self.clickDeleteButton()
            
            #Click OK button on CRM pop up
            self.clickOKButton()
            #wait for purchase request deleted
            wait(2)
        else:
            logInfo("The purchase does not exist in the system")
        
