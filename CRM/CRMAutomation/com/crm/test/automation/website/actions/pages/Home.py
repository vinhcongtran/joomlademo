# coding=utf-8
'''
Created on Nov 9, 2015

@author: phuong.dang
'''

from com.crm.test.automation.website.actions.AbstractPage import AbstractPage
from com.crm.test.automation.website.actions.Common import logInfo, \
    logWarning, getPSTDate, getPSTMonth, getPSTYear, wait
from com.crm.test.automation.website.interfaces.HomePage import HomePage


class Home(AbstractPage, HomePage):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        AbstractPage.__init__(self)
        HomePage.__init__(self)
        
    #####################
    # Click actions
    #####################
        
    def clickThumbnail(self, thumbnailName):
        element = self.btnThumbnailByName.replace("$THUMBNAIL_NAME$", thumbnailName)
        self.click(element)
           
    