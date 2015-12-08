'''
Created on Dec 8, 2015

@author: van.ngo
'''

from time import strftime, localtime
import unittest
import HTMLTestRunner
from ABT.Modules.Common.ImportPages import ImportPages


class Ex03Article(unittest.TestCase, ImportPages):
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
        self.status = None
        self.imgInsert = "powered_by.png"
        self.browser = None


    def tearDown(self):
        #End conditions
        self.deleteArticle(self.browser, self.title)
        self.logOut(self.browser)
        self.browser.quit()
    
    def test_TC05ArticlePaging(self):
        # Main steps
        self.browser = self.openBrowser()
        
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.browser = self.navigate(self.browser, self.joomlaUrl)
           
        self.logInfo("Step 2 - Enter valid username into Username field")
        self.logInfo("Step 3 - Enter valid password into Password field")
        self.logInfo("Step 4 - Click on 'Log in' button")
        self.login(self.browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(self.browser, "Content>Article Manager")
  
        self.logInfo("Step 6 -  Select '5' item of the 'Display' dropdown list at the footer section of the article table ")
        self.pagingArticle(self.browser, '5')
        
        #VP: 1. "Article successfully saved" message is displayed
        self.logInfo("Step 7 -  Verify the article table is paging into 5 articles per page ")
        self.checkPagingArticle(self.browser, 5)
        
        self.logInfo("Step 8 -  Select 'All' item of the 'Display' dropdown list at the footer section of the article table")
        self.pagingArticle(self.browser, 'All')
        
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 9 -  Verify all articles are displayed in one page ")
        self.checkAllArticleDisplay(self.browser)
        
    def test_TC06ArticleAddImage(self):
        # Main steps
        self.browser = self.openBrowser()
        
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.browser = self.navigate(self.browser, self.joomlaUrl)
           
        self.logInfo("Step 2 - Enter valid username into Username field")
        self.logInfo("Step 3 - Enter valid password into Password field")
        self.logInfo("Step 4 - Click on 'Log in' button")
        self.login(self.browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(self.browser, "Content>Article Manager")
  
        self.logInfo("Step 6 -  Click on 'New' icon of the top right toolbar ")
        self.logInfo("Step 7 -  Enter a title on 'Title' text field ")
        self.logInfo("Step 8 -  Select an item from the 'Category' dropdown list ")
        self.logInfo("Step 9 -  Enter value on 'Article Text' text area ")
        self.logInfo("Step 10 - Click on 'Image' button ")
        self.logInfo("Step 11 - Select 'powered_by.pnj' image from the 'Image' dialog ")
        self.logInfo("Step 12 - Click on 'Insert' button ")
        self.logInfo("Step 13 - Click on 'Save & Close' icon of the top right toolbar ")
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option, self.status, self.imgInsert)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)  
        
if __name__ == '__main__':

    tests = ['test_TC05ArticlePaging','test_TC06ArticleAddImage']
    
    for testcase in tests:
        suite = unittest.TestSuite()
        suite.addTest(Ex03Article(testcase))
        dateTimeStamp = strftime("%Y%m%d %H%M%S", localtime())
        buf = file("D:\\Log\EX03TestReport" + "_" + dateTimeStamp + ".html", "wb")
        runner = HTMLTestRunner.HTMLTestRunner(
                            stream=buf,
                            title=testcase + 'Exercise 03 - Test Results',
                            description=testcase + ' result'
                            )
        
        runner.run(suite)
