'''
Created on Dec 8, 2015

@author: van.ngo
'''
from time import strftime, localtime
import unittest
from unittest.runner import TextTestRunner
from ABT.Modules.Common.ImportPages import ImportPages



class Ex02Article(unittest.TestCase, ImportPages):
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
        
        self.newtitle = "Edit Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.newcategory = "Components"
        self.newtext = "This is an article after editing"

    def tearDown(self):
        #End conditions
        self.deleteArticle(self.browser, self.title)
        self.logOut(self.browser)
        self.browser.quit()
    
    def test_TC01ArticleCreate(self):
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
        self.logInfo("Step 10 -  Click on 'Save & Close' icon of the top right toolbar ")
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)
    

    def test_TC02ArticleEdit(self):
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
        self.logInfo("Step 9 -  Enter value on 'Article Text' text area ")
        self.logInfo("Step 10 -  Click on 'Save & Close' icon of the top right toolbar ")
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.title)
        
        self.logInfo("Step 12 -  Select Content > Article Manager ")    
        self.navigateMenu(self.browser, "Content>Article Manager")  
        

        self.logInfo("Step 13 -  Check on the recently added article's checkbox ")   
        self.logInfo("Step 14 -  Click on 'Edit' icon of the top right toolbar ")  
        self.logInfo("Step 15 -  Enter a new title on 'Title' text field ")  
        self.logInfo("Step 16 -  Select a new item from the 'Category' dropdown list ")
        self.logInfo("Step 17 -  Enter value on 'Article Text' text area ")  
        self.logInfo("Step 18 -  Click on 'Save & Close' icon of the top right toolbar ")  
        self.editArticle(self.browser, self.title, self.newtitle, self.newcategory, self.newtext, self.option)
        
        #VP: 3. "Article successfully saved" message is displayed
        #VP: 4. Edited article is displayed on the articles table
        self.logInfo("Step 19 -  Verify the article is saved successfully ")  
        self.checkArticleExist(self.browser, self.newtitle)
          
    def test_TC03ArticleDelete(self):
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
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 12 -  Verify the article is saved successfully")  
        self.checkArticleExist(self.browser, self.title)
        
        self.logInfo("Step 13 -  Check on the recently added article's checkbox ")   
        self.logInfo("Step 14 -  Click on 'Trash' icon of the top right toolbar ")   
        self.moveArticleToTrash(self.browser, self.title)
        
        self.logInfo("Step 15 - Verify the confirm message is displayed")
        self.logInfo("Step 16 - Select 'Trash' item of 'Status' dropdown list")
        self.logInfo("Step 17 - Verify the deleted article is displayed on the table grid")
        self.checkArticleMovedToTrash(self.browser, self.title)
        
    
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
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option)
          
           
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
    
#     tests = ["test_TC01ArticleCreate","test_TC02ArticleEdit", "test_TC03ArticleDelete", "test_TO04ArticleSearch"]
    tests = ["test_TC01ArticleCreate", "test_TC03ArticleDelete"]
    suite = unittest.TestSuite(map(Ex02Article, tests))
    runner = TextTestRunner()
    runner.run(suite)
