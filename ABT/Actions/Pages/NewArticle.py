'''
Created on Dec 1, 2015

@author: van.ngo
'''

from selenium.webdriver.remote.webelement import WebElement

from ABT.Actions.CommonActions import CommonActions
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Interfaces.NewArticlePage import NewArticlePage


class NewArticle(CommonActions, NewArticlePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        NewArticlePage.__init__(self)
        CommonActions.__init__(self)
        
      
    ##############################################################################################################
    # Create a new article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title created
    ##############################################################################################################        
    def createNewArticleByButton(self, driver, title, category, text, option, status = None, insert = None, alias = None, access = None, permission = None, featureed = None, language = None):
        #Click on 'New' icon of the top right toolbar
        ManagerArticle().clickToolbarButton(driver, "New")
        
        #Enter value for the new article
        NewArticle().enterValue(driver, title, category, text, status, insert)
        
        #Click option icon to save of the top right toolbar
        option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", option)
        driver.find_element_by_xpath(option).click()
        
        
    ##############################################################################################################
    # Enter values for a new title
    # @param driver: type of browser 
    # @param title, category, ..: information of the title expected to enter 
    ##############################################################################################################                
    def enterValue (self, driver, title, category, text, status = None, insert = None):
        
        driver.find_element_by_xpath(self.txtTitle).clear()
        driver.find_element_by_xpath(self.txtTitle).send_keys(title)
        
        #Select an item from the 'Category' dropdown list
        category = self.ddlCategory.replace("$ITEM NAME$", category)
        driver.find_element_by_xpath(category).click()
        
        #Select status if any
        if (status != None):
            status = self.ddlStatus.replace("$STATUS ITEM$", status)
            driver.find_element_by_xpath(status).click()
        
        #Enter value on 'Article Text' text are
        self.switchToFrame(driver, "jform_articletext_ifr")
        driver.find_element_by_xpath(self.txtText).clear()
        driver.find_element_by_xpath(self.txtText).send_keys(text)
        driver.switch_to.default_content()
        
        #Insert a image
        if (insert != None):
            try:
                driver.find_element_by_xpath(self.btnImage).click()
                imgInsert = self.img.replace("$IMAGE NAME$", insert)
                driver.find_element_by_xpath("//input[@id = 'upload-submit']").click()
                
              
#                 driver.switch
#                 driver.find_element_by_xpath(imgInsert).click()
#                 driver.find_element_by_xpath(self.btnInsert).click()
#                 driver.switch_to.default_content()

            except Exception,e:
                print str(e)
                
                

    ##############################################################################################################
    # Edit an existing article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title edited
    ##############################################################################################################                
    def editArticle(self, driver, title, newtitle, newcategory, newtext, newoption):
        #select Article
        ManagerArticle().selectCheckboxArticle(driver, title)
        ManagerArticle().clickToolbarButton(driver, "Edit")
        #Enter values to edit
        self.enterValue(driver, newtitle, newcategory, newtext)
        
        #Click option icon to save of the top right toolbar
        option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", newoption)
        driver.find_element_by_xpath(option).click()

        

    