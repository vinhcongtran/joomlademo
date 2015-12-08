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
        self.btn = "//div[@id ='toolbar']//a[contains(., '$BUTTON NAME$')]"
        self.msg =  "//div[@id='system-message-container']//li[text() = '$MESSAGE$']"
        self.rowArticle = "//table[@class= 'adminlist']//td[descendant::a[contains(.,'$ARTICLE$')]]"
        self.txtSearch = "//div[@class='filter-search fltlft']//input[@id = 'filter_search']"
        self.btnSearch = "//div[@class='filter-search fltlft']//button[text() = 'Search']"
#         self.lnkArticle = "//table[@class = 'adminlist']//a[contains(.,'"
        self.chkArticle = "//tr[descendant::a[contains(.,'$ARTICLE$')]]//input[@type = 'checkbox']"
        self.ddlStatus = "//select[@name = 'filter_published']/option[contains(.,'$ITEM NAME$')]"
        self.ddlDisplay = "//select[@id = 'limit']//option[text() = '$NUMBER OF ARTICLE$']"
        self.barPage ="//div[@class = 'pagination']//div[@class = 'page']"
        self.tblArticle = "//table[@class= 'adminlist']"