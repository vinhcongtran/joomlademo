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
        
    def checkArticleCreated(self, driver, article):
        
        try:
            driver.find_element_by_xpath(self.msgsuccess)
            print "VP1: PASSED 'Article successfully saved' message displays"
        except:
            print "VP1: FAILED 'Article successfully saved' message does not display"
            
        driver.find_element_by_xpath(self.txtSearch).send_keys(article)
        driver.find_element_by_xpath(self.btnSearch).click()
        try:
            driver.find_element_by_xpath(self.rowArticle + article + "')]]")
            print "VP2: Created article is displayed on the articles table"
        except:
            print "VP2: Created article is not displayed on the articles table"    