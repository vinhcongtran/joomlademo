'''
Created on Dec 1, 2015

@author: van.ngo
'''

from time import strftime, localtime
from ABT.Modules.ImportPages import ImportPages
import unittest
import HTMLTestRunner


class TC01ArticleCreate(unittest.TestCase, ImportPages):
    '''
    classdocs
    '''

    def setUp(self):
        '''
        Constructor
        '''
        ImportPages.__init__(self)
        self.title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.text = "This is an article"
        self.category = "Extensions"
        self.option = "Save & Close"
        self.browser = None
        
    def tearDown(self):
        #End conditions
        self.logOut(self.browser)
        self.browser.quit()
    
    def test_TC01(self):
        # Main steps
        # Open browser
        self.browser = self.openBrowser()
          
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(self.browser, self.joomlaUrl)
          
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(self.browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(self.browser, "Content>Article Manager")
  
        self.logInfo("Step 6,7,8,9,10: Create a new article ")
        self.createNewArticle(self.browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)
    
    def test_TC02(self):
        # Main steps
        # Open browser
        self.browser = self.openBrowser()
          
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(self.browser, self.joomlaUrl)
          
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(self.browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(self.browser, "Content>Article Manager")
  
        self.logInfo("Step 6,7,8,9,10: Create a new article ")
        self.createNewArticle(self.browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TC01ArticleCreate('test_TC01'))
    suite.addTest(TC01ArticleCreate('test_TC02'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#     unittest.main(suite)
    buf = file("D:\\testcase01.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='TC01 - Test Results',
                    description='TC01 result'
                    )
    runner.run(suite)
