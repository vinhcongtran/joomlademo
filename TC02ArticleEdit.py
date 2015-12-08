'''
Created on Dec 2, 2015

@author: van.ngo
'''
from time import strftime, localtime
from ABT.Modules.Common.ImportPages import ImportPages



class TC02ArticleEdit(ImportPages):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ImportPages.__init__(self)
        self.title = "Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.text = "This is an article"
        self.category = "Extensions"
        self.option = "Save & Close"
        
        self.newtitle = "Edit Article " + strftime("%Y-%m-%d %H:%M:%S", localtime())
        self.newcategory = "Components"
        self.newtext = "This is an article after editing"
    
    
    def TC02(self):
        # Main steps
        # Open browser
        browser = self.openBrowser()
          
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(browser, self.joomlaUrl)
          
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(browser, self.username, self.password)
          
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(browser, "Content>Article Manager")
  
        self.logInfo("Step 6,7,8,9,10 -  Create a new article ")
        self.createNewArticle(browser, self.title, self.category, self.text, self.option)
          
        #VP: 1. "Article successfully saved" message is displayed
        #VP: 2. Created article is displayed on the articles table
        self.logInfo("Step 11 -  Verify the article is saved successfully ")  
        self.checkArticleExist(browser, self.title)
        
        self.logInfo("Step 12 -  Select Content > Article Manager ")    
        self.navigateMenu(browser, "Content>Article Manager")  
        

        self.logInfo("Step 13,14,15,16,17,18 -  Check on the recent checkbox and Edit it ")   
        self.editArticle(browser, self.title, self.newtitle, self.newcategory, self.newtext, self.option)
        
        #VP: 3. "Article successfully saved" message is displayed
        #VP: 4. Edited article is displayed on the articles table
        self.logInfo("Step 19 -  Verify the article is saved successfully ")  
        self.checkArticleExist(browser, self.newtitle)
          
        #End conditions
        self.logOut(browser)
        browser.quit()  
    
    

if __name__ == '__main__':
    TC02ArticleEdit().TC02()