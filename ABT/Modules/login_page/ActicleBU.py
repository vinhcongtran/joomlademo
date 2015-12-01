'''
Created on Dec 1, 2015

@author: van.ngo
'''



from time import strftime, localtime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from ABT.Actions.Common import Common
from ABT.Actions.Pages.NewArticle import NewArticle
from ABT.Actions.Pages.ControlPanel import ControlPanel
from ABT.Actions.Pages.Login import Login
from ABT.Actions.Pages.ManagerArticle import ManagerArticle


class ActicleBU(Login, ControlPanel, Common, NewArticle, ManagerArticle):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Login.__init__(self)
        ControlPanel.__init__(self)
        Common.__init__(self)
        NewArticle.__init__(self)
        ManagerArticle.__init__(self)
        self.title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.text = "This is an article"
        self.category = "Extensions"
    
    
    def TC01(self):
        # Main steps
        # Open browser
        browser = self.openBrowser()
        
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(browser, "http://192.168.189.207/joomla/administrator/index.php")
        
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(browser, "admin", "admin")
        
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(browser, "Content>Article Manager")

        self.logInfo("Step 6,7,8,9,10: Create a new article ")
        self.createNewArticle(browser, self.title, self.category, self.text)
        
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.checkArticleCreated(browser, self.title)
#         
        
if __name__ == '__main__':
    ActicleBU().TC01()