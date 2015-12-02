'''
Created on Dec 2, 2015

@author: van.ngo
'''
from time import strftime, localtime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


from ABT.Actions.Pages.NewArticle import NewArticle
from ABT.Actions.Pages.ControlPanel import ControlPanel
from ABT.Actions.Pages.Login import Login
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Actions.CommonActions import CommonActions


class TC03ArticleDelete(Login, ControlPanel, CommonActions, NewArticle, ManagerArticle):
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
        self.status = "Unpublished"

    
    def TC03(self):
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
        
        self.logInfo("Step 13,14 -  Check on the recent checkbox and move it to Trash ")   
        self.deleteArticle(browser, self.title)
        
        self.logInfo("Step 15 - Verify the confirm message is displayed")
        self.checkSuccessMessage(browser, "1 article trashed.")
          
        #End conditions
        self.logOut(browser)
        browser.quit()  
    
    

if __name__ == '__main__':
    TC03ArticleDelete().TC03()
