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
        button = self.btnToolBar.replace("$BUTTON NAME$", button)
        driver.find_element_by_xpath(button).click()
     
     
    ##############################################################################################################
    # Check a message displayed 
    # @param driver: type of browser 
    # @param message: message expected to check
    ############################################################################################################## 
    def checkMessageDisplay(self, driver, message):  
        msg = self.lblMessage.replace("$MESSAGE$", message)
        self.verifyTrue(self.doesElementDisplay(driver, msg), "\tPASSED : " + message + " message displays", "FAILED : " + message + " message does not display")
        
          
    ##############################################################################################################
    # Check an article existed 
    # @param driver: type of browser 
    # @param article: article expected to check
    ##############################################################################################################    
    def checkArticleCreated(self, driver, article):       
            self.verifyTrue(self.doesArticleExist(driver, article) == True, "\tPASSED : the created '" + article + "' article exists on the articles table", "\tFAILED : the created '" + article + "' article does not exist on the articles table"  )
            
            
    ##############################################################################################################
    # Check an existing article edited 
    # @param driver: type of browser 
    # @param article: article expected to check
    ##############################################################################################################    
    def checkArticleEdited(self, driver, article):       
            self.verifyTrue(self.doesArticleExist(driver, article) == True, "\tPASSED : the edited '" + article + "' article exists on the articles table", "\tFAILED : the edited '" + article + "' article does not exist on the articles table"  )
            
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
        except:
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
                if (self.doesArticleExist(driver, title)):
                    existInTrash = self.DoesArticleMoveToTrash(driver, title)
                    if existInTrash == True:
                        ManagerArticle().selectCheckboxArticle(driver, title)
                        ManagerArticle().clickToolbarButton(driver, "Empty trash")
                        self.logInfo("=========Cleared test environment===========")
                        
                    else:
                        status = self.ddlStatus.replace("$ITEM NAME$", "All")
                        driver.find_element_by_xpath(status).click()
                
                        self.moveArticleToTrash(driver, title)
                    
                        status = self.ddlStatus.replace("$ITEM NAME$", "Trashed")
                        driver.find_element_by_xpath(status).click()
                    
                        ManagerArticle().selectCheckboxArticle(driver, title)
                        ManagerArticle().clickToolbarButton(driver, "Empty trash")    
                        self.logInfo("=========Cleared test environment===========")
                else:
                    self.logInfo("=========Cleared test environment===========")   
                return None
        except Exception, e:
            print str(e)
        
        
        
    ##############################################################################################################
    # Check entered keywords contained in displayed titles
    # @param driver: type of browser 
    # @param keywords: keywords expected to be a parts of displayed titles
    ##############################################################################################################                         
    def checkTextContains(self, driver, keywords):
            table = driver.find_element_by_xpath(self.tblArticle)
            tablecontent = table.text
            self.verifyIn(keywords, tablecontent, "\tPASSED: The " + keywords + "displays in the table", "\tFAILED: The " + keywords + "does not display in the table")

    ##############################################################################################################
    # Check to see if a text is contained in a table finding by xpath
    # @param driver: type of browser 
    # @param text: keywords expected to be a parts of displayed titles
    # @param xPathTable: it should be a xPath of table
    # Return True if the text contains in table, False if it does not contain in table
    ##############################################################################################################                         
    def DoesTextContains(self, driver, text, xPathTable):
        try:
            table = driver.find_element_by_xpath(xPathTable)
            tablecontent = table.text
            if text in tablecontent:
                return True
            else:
                return False   
        except Exception,e:
            print str(e)
    ##############################################################################################################
    # Select the number of articles to display
    # @param driver: type of browser 
    # @param number: the number of articles want to display
    ##############################################################################################################                                
    def pageArticles(self, driver, number):
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
        try:
            tblArticleRow = self.tblArticle + "/tr"
            rowCount = len(driver.find_elements_by_xpath(tblArticleRow))
            self.verifyTrue(number == rowCount, "\tPASSED: The article table is paging into %s articles per page" %number, "\tFAILED: The article table is paging into %s articles per page instead of %s" %(rowCount,number))
        except Exception, e:
            print str(e)
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

    def DoesArticleMoveToTrash(self, driver, title):
        status = self.ddlStatus.replace("$ITEM NAME$", "Trashed")
        driver.find_element_by_xpath(status).click()
        self.DoesTextContains(driver, title, self.tblArticle)
    
    ##############################################################################################################
    # Click on status icon of a article
    # @param driver: type of browser 
    # @param title: the title expected to click on its status icon
    ##############################################################################################################           
    def clickStatusIcon (self, driver, title):
        icnStatus = self.icnStatus.replace("$ARTICLE$", title)
        driver.find_element_by_xpath(icnStatus).click()     

    def clickFeatureIcon (self, driver, title):
        icnFeature = self.imgFeaturedToggle.replace("$ARTICLE$", title)
        driver.find_element_by_xpath(icnFeature).click()
        
    def checkArticleStatus(self, driver, title , status):
        txtStatus = self.txtStatus.replace("$ARTICLE$", title)       
        stt = driver.find_element_by_xpath(txtStatus).get_attribute("textContent")
        self.verifyTrue(stt == status, "\tPASSED: The icon of the selected item is showed as '" + status + "'", "\tFAILED: The icon of the selected item is NOT showed as '" + status +"'")

    def checkArticleFeature (self, driver, title , sttFeature ):
        
        