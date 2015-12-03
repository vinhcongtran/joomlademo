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

    ##############################################################################################################
    # Click a button on Toolbar
    # @param driver: type of browser 
    # @param button: button expected to click
    ##############################################################################################################
    def clickToolbarButton (self, driver, button):
        driver.find_element_by_xpath(self.btn + button + "')]").click()
     
     
    ##############################################################################################################
    # Check a message displayed 
    # @param driver: type of browser 
    # @param message: message expected to check
    ############################################################################################################## 
    def checkSuccessMessage(self, driver, message):  
        try:
            driver.find_element_by_xpath(self.msgSuccess + message + "']")
            print "\tPASSED : " + message + " message displays"
        except:
            print "FAILED : " + message + " message does not display"
        
          
    ##############################################################################################################
    # Check an article existed 
    # @param driver: type of browser 
    # @param article: article expected to check
    ##############################################################################################################    
    def checkArticleExist(self, driver, article):
        
        ManagerArticle().checkSuccessMessage(driver, "Article successfully saved")
            
        exist = self.searchArticle(driver, article)
        if (exist):
            print "\tPASSED : " + article + " article exists on the articles table"
        else:
            print "FAILED : '" + article + "' created article does not exist on the articles table"    
        
            
    ##############################################################################################################
    # Search an article by title 
    # @param driver: type of browser 
    # @param title: title expected to search
    ##############################################################################################################     
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
    
    
    ##############################################################################################################
    # Select on checkbox of the first article
    # @param driver: type of browser 
    ##############################################################################################################            
    def selectFirstArticle (self, driver):
        driver.find_element_by_xpath(self.cboFirstArticle).click()


    ##############################################################################################################
    # Move an article to Trash
    # @param driver: type of browser 
    # @param title: title expected to delete
    ##############################################################################################################                
    def deleteArticle(self, driver, title):
        try:
            if (ManagerArticle().searchArticle(driver, title)):
                ManagerArticle().selectFirstArticle(driver)
                ManagerArticle().clickToolbarButton(driver, "Trash")
            else:
                "The article" + title + "does not exist to delete"
        except:
            print "Please create an article before deleting it"
        
           
    ##############################################################################################################
    # Check entered keywords be a part of displayed titles
    # @param driver: type of browser 
    # @param keywords: keywords expected to be a parts of displayed titles
    ##############################################################################################################                         
    def checkTextContains(self, driver, keywords):
        try:
            table = driver.find_element_by_xpath("//table[@class = 'adminlist']//tbody")
            tablecontent = table.text
            if keywords in tablecontent:
                print "\tPASSED: The titles of displayed articles are partially matched with the entered keyword"
            return True;
        except:
            print "\tFAILED: The titles of displayed articles are not partially matched with the entered keyword"
            return False;

