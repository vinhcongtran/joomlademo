'''
Created on Dec 11, 2015

@author: van.ngo
'''

from time import strftime, localtime
import unittest
from unittest.runner import TextTestRunner



class Ex05Article(unittest.TestCase, AbstractTest):
    '''
    classdocs
    '''

    def setUp(self):
        '''
        Constructor
        '''
        
        self.title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.text = "This is an article"
        self.category = "Extensions"
        self.status = None
        self.insert = None
        self.access = "Public"
        self.option = "Save & Close"
        self.browser = self.openBrowser()
        self.sttUnpublished = "Unpublished"
        self.sttPublished = "Published"
        self.sttFeatured = "Featured article"
        self.sttUnFeatured = "Unfeatured article"


    def tearDown(self):
        #End conditions
        self.deleteArticle(self.browser, self.title)
        self.logOut(self.browser)
        self.browser.quit()
    
    
    def test_TC07ArticleChangeStatus(self):
        # Main steps 
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
        self.checkMessageDisplay(self.browser, "Article successfully saved")
        self.checkArticleCreated(self.browser, self.title)
        
        self.logInfo("Step 13 -  Check on the recently added article's checkbox") 
        self.selectCheckboxArticle(self.browser, self.title)
        
        self.logInfo("Step 14 -  Click on the status icon of the selected article in the Status column") 
        self.clickStatusIcon(self.browser, self.title)

        self.logInfo("Step 15 -  Verify the article is unpublished successfully") 
        #VP: 1. The icon of the selected item is showed as 'Unpublished'. 
        self.checkMessageDisplay(self.browser, "1 article unpublished")
        #VP: 2. The "1 article unpublished" message is displayed
        self.checkArticleStatus(self.browser, self.title, self.sttUnpublished)

        self.logInfo("Step 16 -  Check on the recently added article's checkbox") 
        self.selectCheckboxArticle(self.browser, self.title)
        
        self.logInfo("Step 17 -  Click on the status icon of the selected article in the Status column") 
        self.clickStatusIcon(self.browser, self.title)

        self.logInfo("Step 18 -  Verify the article is published successfully")
        #VP: 1. The icon of the selected item is showed as 'Publish'. 
        self.checkMessageDisplay(self.browser, "1 article published")
        #VP: 2. The "1 article published" message is displayed     
        self.checkArticleStatus(self.browser, self.title, self.sttPublished)


    def test_TC08ArticleChangeFeature(self):
        # Main steps 
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
          
        self.logInfo("Step 12 -  Verify the article is saved successfully") 
        #VP: "Article successfully saved" message is displayed
        self.checkMessageDisplay(self.browser, "Article successfully saved")
        #VP: Created article is displayed on the articles table 
        self.checkArticleCreated(self.browser, self.title)
        
        self.logInfo("Step 13 -  Check on the recently added article's checkbox") 
        self.selectCheckboxArticle(self.browser, self.title)
        
        self.logInfo("Step 14 -  Click on the status icon of the selected article in the Featured column") 
        self.clickFeatureIcon(self.browser, self.title)
        #VP: The icon of the selected item is showed as 'Featured'. 
        self.checkArticleFeatureIconStatus(self.browser, self.title, self.sttFeatured)

        self.logInfo("Step 15 -  Verify the article is featured successfully") 
        self.checkArticleFeature(self.browser, self.title, "Featured")

        self.logInfo("Step 16 -  Check on the recently added article's checkbox") 
        self.selectCheckboxArticle(self.browser, self.title)
         
        self.logInfo("Step 17 -  Click on the status icon of the selected article in the Featured column") 
        self.clickFeatureIcon(self.browser, self.title)
        #VP: The icon of the selected item is showed as 'Unfeatured'. 
        self.checkArticleFeatureIconStatus(self.browser, self.title, self.sttUnFeatured)
         
        self.logInfo("Step 18 -  Verify the article is featured successfully")
        self.checkArticleFeature(self.browser, self.title, "Unfeatured")

    def test_TC09ArticleCreateWithAccessLevel(self):
        # Main steps 
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
        self.logInfo("Step 10 -  Select 'Public' item from the 'Access' dropdown list ")
        self.logInfo("Step 11 -  Click on 'Save & Close' icon of the top right toolbar ")
        self.createNewArticleByButton(self.browser, self.title, self.category, self.text, self.option, self.status, self.insert, self.access)
        
        self.logInfo("Step 12 -  Verify the article is saved successfully") 
        #VP: 1. "Article successfully saved" message is displayed
        self.checkMessageDisplay(self.browser, "Article successfully saved")
        #VP: 2. Created article is displayed on the articles table
        self.checkArticleCreated(self.browser, self.title)
        #VP: 3. The Access Level of the article is displayed as 'Public'
        self.checkAccessLevelValue(self.browser, self.title, "Access", "Public")
        #VP: 4. Created article's information is displayed correctly
        self.checkArticleInformation(self.browser, self.title, self.title, self.category, self.text, self.access)

if __name__ == '__main__':
    tests = ["test_TC07ArticleChangeStatus", "test_TC08ArticleChangeFeature", "test_TC09ArticleCreateWithAccessLevel"]
    suite = unittest.TestSuite(map(Ex05Article, tests))
    runner = TextTestRunner()
    runner.run(suite)

        