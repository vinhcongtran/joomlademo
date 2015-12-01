'''
Created on Dec 1, 2015

@author: van.ngo
'''

class NewActiclePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        txttitle = "//ul[@class = 'adminformlist']//input[@class= 'inputbox required']"
        ddlcategory = "//select[@name='jform[catid]']/option[contains(.,'Extensions')]"
        txttext = "html/body"
        btnsaveandclose = "//div[@id = 'toolbar']//li[@id = 'toolbar-save']//a[normalize-space() = 'Save & Close']"
        