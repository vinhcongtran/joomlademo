'''
Created on Dec 2, 2015

@author: van.ngo
'''
from _ast import Assert
from cgitb import text
from time import strftime, localtime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from ABT.Actions.CommonActions import CommonActions
from ABT.Actions.Pages.ControlPanel import ControlPanel
from ABT.Actions.Pages.Login import Login
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Actions.Pages.NewArticle import NewArticle


class TC04ArticleSearch(Login, ControlPanel, CommonActions, NewArticle, ManagerArticle):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Login.__init__(self)
        ControlPanel.__init__(self)
        CommonActions.__init__(self)
        NewArticle.__init__(self)
        ManagerArticle.__init__(self)
        self.title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.text = "This is an article"
        self.category = "Extensions"
        self.option = "Save & Close"
        self.status = "Published"
    
    
    def TC04(self):
        
        # Main steps
        # Open browser
        browser = self.openBrowser()
          
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(browser, self.joomlaUrl)
          
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(browser, "Content>Article Manager")
  
        self.logInfo("Step 6,7,8,9,10, 11 -  Create a new article ")
        self.createNewArticle(browser, self.title, self.category, self.text, self.option, self.status)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 12 -  Verify the article is saved successfully ")  
        self.checkArticleExist(browser, self.title)

        self.logInfo("Step 13,14 -  Search the recent created article ")  
        self.searchArticle(browser, self.title)
        
        list = browser.find_elements_by_xpath("//table[@class = 'adminlist']")
        print list
        Assert.assertTrue(self.title, list.size() > 0)
        
         
#         #End conditions
#         self.logOut(browser)
#         browser.quit()
         
        
if __name__ == '__main__':
    TC04ArticleSearch().TC04()
