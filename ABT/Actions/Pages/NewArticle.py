'''
Created on Dec 1, 2015

@author: van.ngo
'''
from ABT.Interfaces.NewArticlePage import NewActiclePage
from ABT.Actions.Pages.ManagerArticle import ManagerArticle

class NewArticle(NewActiclePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        NewActiclePage.__init__(self)
        ManagerArticle.__init__(self)
        
    def crearNewArticle(self, driver, title, category, text):
        #Click on 'New' icon of the top right toolbar
        ManagerArticle.clickNew(self, driver)
        
        #Enter a title on 'Title' field
        driver.find_element_by_xpath(self.).send_keys(title)
        
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath(self.txttitle).send_keys(title)
        driver.switch_to.default_content()
    