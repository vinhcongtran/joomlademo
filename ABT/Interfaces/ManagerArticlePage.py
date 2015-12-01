'''
Created on Dec 1, 2015

@author: van.ngo
'''

class ManagerArticlePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.btnnew = "//div[@id = 'toolbar']//li[@id = 'toolbar-new']//a[normalize-space() = 'New']"
        self.msgsuccess =  "//div[@id='system-message-container']//li[text() = 'Article successfully saved']"
        self.rowArticle = "//table[@class= 'adminlist']//td[descendant::a[contains(.,'"
        self.txtSearch = "//div[@class='filter-search fltlft']//input[@id = 'filter_search']"
        self.btnSearch = "//div[@class='filter-search fltlft']//button[text() = 'Search']"