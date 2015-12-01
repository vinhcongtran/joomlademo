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
      
        
    def createNewArticle(self, driver, title, category, text, alias = None, status = None, access = None, permission = None, featureed = None, language = None):
        #Click on 'New' icon of the top right toolbar
        ManagerArticle().clickNew(driver)
        
        #Enter a title on 'Title' field
        driver.find_element_by_xpath(self.txtTitle).send_keys(title)
        
        #Select an item from the 'Category' dropdown list
        driver.find_element_by_xpath(self.ddlCategory + category + "')]").click()
       
        
        #Enter value on 'Article Text' text are
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath(self.txtText).send_keys(text)
        driver.switch_to.default_content()
        
        #Click on 'Save & Close' icon of the top right toolbar
        driver.find_element_by_xpath(self.btnSaveAndClose).click()
        
    