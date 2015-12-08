'''
Created on Dec 2, 2015

@author: van.ngo
'''
from time import strftime, localtime
import unittest
import HTMLTestRunner
from ABT.Modules.Common.ImportPages import ImportPages

class TC04ArticleSearch(unittest.TestCase, ImportPages):
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
        self.status = "Unpublished"
        
    def tearDown(self):
        #End conditions
        self.logOut(self.browser)
        self.browser.quit()
    
    
    
    def test_TO04ArticleSearch(self):
        
        # Main steps
        # Open browser
        self.browser = self.openBrowser()
          
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(self.browser, self.joomlaUrl)
          
        self.logInfo("Step 2 - Enter valid username into Username field")
        self.logInfo("Step 3 - Enter valid password into Password field")
        self.logInfo("Step 4 - Click on 'Log in' button")
        self.login(self.browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(self.browser, "Content>Article Manager")
  
        self.logInfo("Step 6 -  Click on 'New' icon of the top right toolbar ")
        self.logInfo("Step 7 -  Enter a title on 'Title' text field ")
        self.logInfo("Step 8 -  Select an item from the 'Category' dropdown list ")
        self.logInfo("Step 9 -  Select 'Published' item from 'Status' dropdown list ")
        self.logInfo("Step 10 -  Enter value on 'Article Text' text area ")
        self.logInfo("Step 11 -  Click on 'Save & Close' icon of the top right toolbar ")
        self.createNewArticle(self.browser, self.title, self.category, self.text, self.option)
          
           
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 12 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)
 
        self.logInfo("Step 13 -  Search the recent created article ") 
        self.logInfo("Step 14 -  Click on 'Search' button ") 
        self.searchArticle(self.browser, self.title)
        
        #VP: 3. Verify the titles of displayed articles are partially matched with the entered keyword
        self.logInfo("Step 15-  Verify the titles of displayed articles are partially matched with the entered keyword ")         
        self.checkTextContains(self.browser, self.title)

        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TC04ArticleSearch('test_TO04ArticleSearch'))

#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#     unittest.main(suite)
    buf = file("D:\\testcase01.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=buf, title='TC01 - Test Results',
                    description='TC01 result'
                    )
    runner.run(suite)
