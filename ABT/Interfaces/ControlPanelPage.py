'''
Created on Dec 1, 2015

@author: van.ngo
'''

class ControlPanelPage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.pagUnique = "//title[text()='Joomla - Administration - Control Panel']"
        self.itemcontent = "//div[@id = 'module-menu']//a[text() = 'Content']"
        self.itemacticle = "//div[@id = 'module-menu']//a[text() = 'Article Manager']"