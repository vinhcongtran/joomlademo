# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.EditPurchaseRequestPage import EditPurchaseRequestPage


class EditPurchaseRequest(AbstractPage, EditPurchaseRequestPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        EditPurchaseRequestPage.__init__(self)
        
    #####################
    # Check actions
    #####################
    def checkTheCorrespondingEditPurchasePageIsDisplayed(self):
        self.verifyTrue(self.doesElementExisted(self.pagUnique), "Edit Purchase Request page displays", "Edit Purchase Request page DOES NOT display")

    #####################
    # Click actions
    #####################
    def clickCancelButton(self):
        self.click(self.btnCancel)