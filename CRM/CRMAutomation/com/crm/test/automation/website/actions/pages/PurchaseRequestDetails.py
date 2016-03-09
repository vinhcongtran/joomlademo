# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.PurchaseRequestDetailsPage import PurchaseRequestDetailsPage


class PurchaseRequestDetails(AbstractPage, PurchaseRequestDetailsPage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        PurchaseRequestDetailsPage.__init__(self)
        

    #####################
    # Click actions
    #####################
    def clickEditButton(self):
        self.click(self.btnEdit)