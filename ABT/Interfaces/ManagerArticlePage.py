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
        self.btn = "//div[@id ='toolbar']//a[contains(., '"
        self.msgSuccess =  "//div[@id='system-message-container']//li[text() = '"
        self.rowArticle = "//table[@class= 'adminlist']//td[descendant::a[contains(.,'"
        self.txtSearch = "//div[@class='filter-search fltlft']//input[@id = 'filter_search']"
        self.btnSearch = "//div[@class='filter-search fltlft']//button[text() = 'Search']"
        self.lnkArticle = "//table[@class = 'adminlist']//a[contains(.,'"
        self.cboFirstArticle = "//table[@class = 'adminlist']//input[@id= 'cb0']"