'''
Created on Dec 1, 2015

@author: van.ngo
'''
from ABT.Interfaces.NewArticlePage import NewArticlePage
from ABT.Actions.Pages.ManagerArticle import ManagerArticle


class NewArticle(NewArticlePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        NewArticlePage.__init__(self)
      
    ##############################################################################################################
    # Create a new article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title created
    ##############################################################################################################        
    def createNewArticle(self, driver, title, category, text, option, status = None, alias = None, access = None, permission = None, featureed = None, language = None):
        #Click on 'New' icon of the top right toolbar
        ManagerArticle().clickToolbarButton(driver, "New")
        
        #Enter value for the new articel
        NewArticle().enterValue(driver, title, category, text, status)
        
        #Click option icon to save of the top right toolbar
        driver.find_element_by_xpath(self.btnToolbarBox + option + "']").click()
        
        
    ##############################################################################################################
    # Enter values for a new title
    # @param driver: type of browser 
    # @param title, category, ..: information of the title expected to enter 
    ##############################################################################################################                
    def enterValue (self, driver, title, category, text, status = None):
        
        driver.find_element_by_xpath(self.txtTitle).clear()
        driver.find_element_by_xpath(self.txtTitle).send_keys(title)
        
        #Select an item from the 'Category' dropdown list
        driver.find_element_by_xpath(self.ddlCategory + category + "')]").click()
        
        #Select status if any
        if (status != ""):
            driver.find_element_by_xpath(self.ddlStatus + status + "')]").click()
        
        #Enter value on 'Article Text' text are
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath(self.txtText).clear()
        driver.find_element_by_xpath(self.txtText).send_keys(text)
        driver.switch_to.default_content()


    ##############################################################################################################
    # Edit an existing article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title edited
    ##############################################################################################################                
    def editArticle(self, driver, title, newtitle, newcategory, newtext, newoption):
        #select Article
        ManagerArticle().selectFirstArticle(driver)
        ManagerArticle().clickToolbarButton(driver, "Edit")
        #Enter values to edit
        self.enterValue(driver, newtitle, newcategory, newtext)
        
        #Click option icon to save of the top right toolbar
        driver.find_element_by_xpath(self.btnToolbarBox + newoption + "']").click()

        

    