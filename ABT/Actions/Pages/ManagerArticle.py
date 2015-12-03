'''
Created on Dec 1, 2015

@author: van.ngo
'''
import selenium.common.exceptions

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

    def clickToolbarButton (self, driver, button):
        driver.find_element_by_xpath(self.btn + button + "')]").click()
      
    def checkSuccessMessage(self, driver, message):  
        try:
            driver.find_element_by_xpath(self.msgSuccess + message + "']")
            print "\tPASSED : " + message + " message displays"
        except:
            print "FAILED : " + message + " message does not display"
             
    def checkArticleExist(self, driver, article):
        
        ManagerArticle().checkSuccessMessage(driver, "Article successfully saved")
            
        exist = self.searchArticle(driver, article)
        if (exist):
            print "\tPASSED : " + article + " article exists on the articles table"
        else:
            print "FAILED : '" + article + "' created article does not exist on the articles table"    
            
    def searchArticle(self, driver, title):
        
        driver.find_element_by_xpath(self.txtSearch).clear()
        driver.find_element_by_xpath(self.txtSearch).send_keys(title)
        driver.find_element_by_xpath(self.btnSearch).click()
        try:
            driver.find_element_by_xpath(self.rowArticle + title + "')]]")
            return True;
        except selenium.common.exceptions.NoSuchElementException:
            print "The searched Article does not exist"
            return False;
           
    def selectFirstArticle (self, driver):
        driver.find_element_by_xpath(self.cboFirstArticle).click()

    
    def deleteArticle(self, driver, title):
        try:
            if (ManagerArticle().searchArticle(driver, title)):
                ManagerArticle().selectFirstArticle(driver)
                ManagerArticle().clickToolbarButton(driver, "Trash")
            else:
                "The article" + title + "does not exist to delete"
        except:
            print "Please create an article before deleting it"
        
    def checkTextContains(self, driver, title):
        try:
            table = driver.find_element_by_xpath("//table[@class = 'adminlist']//tbody")
            tablecontent = table.text
            if title in tablecontent:
                print "\tPASSED: The titles of displayed articles are partially matched with the entered keyword"
            return True;
        except:
            print "\tFAILED: The titles of displayed articles are not partially matched with the entered keyword"
            return False;

