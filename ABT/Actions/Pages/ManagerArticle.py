'''
Created on Dec 1, 2015

@author: van.ngo
'''
import selenium.common.exceptions

from ABT.Interfaces.ManagerArticlePage import ManagerArticlePage
from ABT.Actions.CommonActions import CommonActions


class ManagerArticle(ManagerArticlePage, CommonActions):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        ManagerArticlePage.__init__(self)
        CommonActions.__init__(self)
        
    
    ##############################################################################################################
    # Click a button on Toolbar
    # @param driver: type of browser 
    # @param button: button expected to click
    ##############################################################################################################
    def clickToolbarButton (self, driver, button):
        button = self.btn.replace("$BUTTON NAME$", button)
        driver.find_element_by_xpath(button).click()
     
     
    ##############################################################################################################
    # Check a message displayed 
    # @param driver: type of browser 
    # @param message: message expected to check
    ############################################################################################################## 
    def checkMessageDisplay(self, driver, message):  
        msg = self.msg.replace("$MESSAGE$", message)
        try:
            driver.find_element_by_xpath(msg)
            print "\tPASSED : " + message + " message displays"
        except:
            print "FAILED : " + message + " message does not display"
        
          
    ##############################################################################################################
    # Check an article existed 
    # @param driver: type of browser 
    # @param article: article expected to check
    ##############################################################################################################    
    def checkArticleExist(self, driver, article):
        
        ManagerArticle().checkMessageDisplay(driver, "Article successfully saved")
            
        if (self.doesArticleExist(driver, article)):
            print "\tPASSED : " + article + " article exists on the articles table"
        else:
            print "\tFAILED : '" + article + "' created article does not exist on the articles table"    
        
            
    ##############################################################################################################
    # Search an article by title 
    # @param driver: type of browser 
    # @param title: title expected to search
    ##############################################################################################################     
    def searchArticle(self, driver, title):
        try:
            driver.find_element_by_xpath(self.txtSearch).clear()
            driver.find_element_by_xpath(self.txtSearch).send_keys(title)
            driver.find_element_by_xpath(self.btnSearch).click()
        except Exception,e:
            print str(e)
         
            
    ##############################################################################################################
    # Check to see a article exist or not 
    # @param driver: type of browser 
    # @param title: title expected to search
    # return : False if the article does not exist
    ##############################################################################################################              
    def doesArticleExist(self, driver, title):
        self.searchArticle(driver, title)
        try:
            article = self.rowArticle.replace("$ARTICLE$", title)
            driver.find_element_by_xpath(article)
            return True
        except Exception,e:
            print str(e)
            return False
    
    ##############################################################################################################
    # Select on checkbox of the first article
    # @param driver: type of browser 
    # @param article : article would like to check on
    ##############################################################################################################            
    def selectCheckboxArticle(self, driver, article):
        chkArticle = self.chkArticle.replace("$ARTICLE$", article)
        driver.find_element_by_xpath(chkArticle).click()


    ##############################################################################################################
    # Move an article to Trash
    # @param driver: type of browser 
    # @param title: title expected to delete
    ##############################################################################################################                
    def moveArticleToTrash(self, driver, title):
        try:
            self.searchArticle(driver, title)
            if (self.doesArticleExist(driver, title)):
                ManagerArticle().selectCheckboxArticle(driver, title)
                ManagerArticle().clickToolbarButton(driver, "Trash")
            else:
                "The article" + title + "does not exist to move to Trash"
        except Exception, e:
            print str(e)
            print "Please create an article before moving it to Trash"


    ##############################################################################################################
    # Check a article moved to trash
    # @param driver: type of browser 
    # @param title: title expected to delete
    ##############################################################################################################          
    def checkArticleMovedToTrash(self, driver, title):
        #Verify the confirm message is displayed
        self.checkMessageDisplay(driver, "1 article trashed.")
        
        #Verify the trashed article is displayed on the table grid
        status = self.ddlStatus.replace("$ITEM NAME$", "Trashed")
        driver.find_element_by_xpath(status).click()
        self.checkTextContains(driver, title)
    
        
    ##############################################################################################################
    # Delete a article forever
    # @param driver: type of browser 
    # @param title: title expected to delete
    ##############################################################################################################      
    def deleteArticle(self, driver, title):
        try:
            self.searchArticle(driver, title)
            if (self.doesArticleExist(driver, title)):
                
                self.moveArticleToTrash(driver, title)
                
                status = self.ddlStatus.replace("$ITEM NAME$", "Trashed")
                driver.find_element_by_xpath(status).click()
                
                ManagerArticle().selectCheckboxArticle(driver, title)
                ManagerArticle().clickToolbarButton(driver, "Empty trash")
                
            self.logInfo("=========Cleared test environment===========")
        except Exception, e:
            print str(e)
        
        
        
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
                print "\tPASSED: The " + keywords + "displays in the table"
        except:
            print "\tFAILED: The " + keywords + "does not display in the table"

        
    ##############################################################################################################
    # Select the number of articles to display
    # @param driver: type of browser 
    # @param number: the number of articles want to display
    ##############################################################################################################                                
    def pagingArticle(self, driver, number):
        try:
            numberOfArticle = self.ddlDisplay.replace('$NUMBER OF ARTICLE$', "%s" %number)
            driver.find_element_by_xpath(numberOfArticle).click()
        except Exception, e:
            print str(e)
            self.logInfo("Cannot select %s" % number)
            
            
    ##############################################################################################################
    # Check to see how many articles displayed after paging
    # @param driver: type of browser 
    # @param number: the number of articles is expected to display after paging
    ##############################################################################################################          
    def checkPagingArticle(self, driver, number):
        tblArticleRow = self.tblArticle + "/tbody/tr"
        rowCount = len(driver.find_elements_by_xpath(tblArticleRow))
        self.verifyTrue(number == rowCount, "\tPASSED: The article table is paging into %s articles per page" %number, "\tFAILED: The article table is paging into %s articles per page instead of %s" %(rowCount,number))

    ##############################################################################################################
    # Check to see if all articles display 
    # @param driver: type of browser 
    ##############################################################################################################           
    def checkAllArticleDisplay (self, driver):
        exist = self.doesElementNotExisted(driver, self.barPage)
        try:
            self.verifyTrue(exist == False, "\tPASSED: All articles are displayed in one page" , "\tFAILED: All articles are not displayed in one page")
        except Exception, e:
            print str(e)
