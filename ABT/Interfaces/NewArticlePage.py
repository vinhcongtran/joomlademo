'''
Created on Dec 1, 2015

@author: van.ngo
'''

class NewArticlePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.txtTitle = "//ul[@class = 'adminformlist']//input[@class= 'inputbox required']"
        self.ddlCategory = "//select[@name='jform[catid]']/option[contains(.,'"
        self.txtText = "html/body"
        self.btnSaveAndClose = "//div[@id = 'toolbar']//li[@id = 'toolbar-save']//a[normalize-space() = 'Save & Close']"
        