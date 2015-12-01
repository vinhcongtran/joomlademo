'''
Created on Dec 1, 2015

@author: van.ngo
'''
from ABT.Interfaces.ManagerArticlePage import ManagerArticlePage


class ManagerArticle(ManagerArticlePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ManagerArticlePage.__init__(self)
    
    def clickNew (self, driver):
        driver.find_element_by_xpath(self.btnnew).click()