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
        self.ddlCategory = "//select[@name='jform[catid]']/option[contains(.,'$ITEM NAME$')]"
        self.txtText = "html/body"
        self.btnToolbarBox = "//div[@id = 'toolbar']//li[@id = 'toolbar-save']//a[normalize-space() = '$TOOLBAR BUTTON NAME$']"
        self.ddlStatus = "//select[@id='jform_state']/option[contains(.,'$STATUS ITEM$')]"
        self.btnImage = "//a[text() = 'Image']"
        self.img = "//div[@class = 'manager']//a[@title = '$IMAGE NAME$']"
        self.btnInsert = "//button[text() = 'Insert']"