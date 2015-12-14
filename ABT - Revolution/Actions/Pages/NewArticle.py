'''
Created on Dec 1, 2015

@author: van.ngo
'''
from selenium.webdriver.support.select import Select

from ABT.Actions.CommonActions import CommonActions
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Interfaces.NewArticlePage import NewArticlePage


class NewArticle(CommonActions, NewArticlePage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        NewArticlePage.__init__(self)
        CommonActions.__init__(self)
        
      
    ##############################################################################################################
    # Create a new article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title created
    ##############################################################################################################        
    def createNewArticleByButton(self, driver, title, category, text, option, status = None, insert = None,  access = None, alias = None, permission = None, featureed = None, language = None):
        #Click on 'New' icon of the top right toolbar
        ManagerArticle().clickToolbarButton(driver, "New")
        
        #Enter value for the new article
        NewArticle().enterValue(driver, title, category, text, status, insert, access)
        
        #Click option icon to save of the top right toolbar
        try:
            option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", option)
            driver.find_element_by_xpath(option).click()
        except Exception, e:
            print str(e)
            
        
    ##############################################################################################################
    # Enter values for a new title
    # @param driver: type of browser 
    # @param title, category, ..: information of the title expected to enter 
    ##############################################################################################################                
    def enterValue (self, driver, title, category, text, status = None, insert = None, access = None):
        
        driver.find_element_by_xpath(self.txtTitle).clear()
        driver.find_element_by_xpath(self.txtTitle).send_keys(title)
        
        #Select an item from the 'Category' dropdown list
        category = self.itmCategory.replace("$ITEM NAME$", category)
        driver.find_element_by_xpath(category).click()
        
        #Select status if any
        if (status != None):
            status = self.ddlStatus.replace("$STATUS ITEM$", status)
            driver.find_element_by_xpath(status).click()
        
        #Enter value on 'Article Text' text are
        self.switchToFrame(driver, "jform_articletext_ifr")
        driver.find_element_by_xpath(self.txtText).clear()
        driver.find_element_by_xpath(self.txtText).send_keys(text)
        driver.switch_to.default_content()
        
        #Insert a image
        if (insert != None):
            self.insertImage(driver, insert)
        
        # Select Access Level if any
        if (access != None):
            access = self.itmAccess.replace("$LEVEL ITEM$", access)
            driver.find_element_by_xpath(access).click()
            
            
    ##############################################################################################################
    # Insert an image into a article
    # @param driver: type of browser 
    # @param image: image expected to insert into a article
    ##############################################################################################################                   
    def insertImage (self, driver, image):
        try:
                driver.find_element_by_xpath(self.btnImage).click()
                imgInsert = self.imgInsert.replace("$IMAGE NAME$", image)
                
                #switch to InsertAndUpload frame
                self.switchToFrameByXpath(driver, self.frmInsertAndUpload)
                #switch to Image frame
                self.switchToFrameByXpath(driver, self.frmImageForm)
                driver.find_element_by_xpath(imgInsert).click()
                driver.switch_to.default_content()
                
                self.switchToFrameByXpath(driver, self.frmInsertAndUpload)
                driver.find_element_by_xpath(self.btnInsert).click()
                driver.switch_to.default_content()


        except Exception,e:
                print str(e)

    ##############################################################################################################
    # Edit an existing article
    # @param driver: type of browser 
    # @param title, category, ..: information of the title edited
    ##############################################################################################################                
    def editArticle(self, driver, title, newtitle, newcategory, newtext, newoption):
        #Search a article before editing
        ManagerArticle().searchArticle(driver, title)
        
        #select Article
        ManagerArticle().selectCheckboxArticle(driver, title)
        ManagerArticle().clickToolbarButton(driver, "Edit")
        
        #Enter values to edit
        self.enterValue(driver, newtitle, newcategory, newtext)
        
        #Click option icon to save of the top right toolbar
        option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", newoption)
        driver.find_element_by_xpath(option).click()
        
        
    ##############################################################################################################
    # Check value of Feature dropdown list of a article, back to Manager Article when finishing checking
    # @param driver: type of browser 
    # @ sttFeature (Featured/Unfeatured): Expected value of Feature dropdown list
    ##############################################################################################################
    def checkArticleFeature (self, driver, title , sttFeature):
        #Search a article before editing
        ManagerArticle().searchArticle(driver, title)
        
        #select Article
        ManagerArticle().selectCheckboxArticle(driver, title)
        ManagerArticle().clickToolbarButton(driver, "Edit")
        
        currentSelection = Select(driver.find_element_by_xpath(self.ddlFeature))
        currentOption = currentSelection.first_selected_option.text
        if sttFeature == "Featured":
            expectedOption = "Yes"
        else:
            expectedOption = "No"
        self.verifyTrue(currentOption == expectedOption, "\tPASSED : The article is %s successfully " %sttFeature , "\tFAILED: The article is NOT %s successfully " %sttFeature)
        
        #Click option icon to save of the top right toolbar
        option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", "Close")
        driver.find_element_by_xpath(option).click()
        
    ##############################################################################################################
    # Check all information of a article displayed correctly
    # @param driver: type of browser 
    # @param title: the title expected to check
    # @param expTitle, expCategory..: expected information of properties
    ##############################################################################################################   
    def checkArticleInformation(self, driver, title, expTitle, expCategory, expText, expAccess):
        titleCorrect = categoryCorrect = textCorrect = accessCorrect = False
        ManagerArticle().selectCheckboxArticle(driver, title)
        ManagerArticle().clickToolbarButton(driver, "Edit")
        
        #Check created title 
        currentTitle = driver.find_element_by_xpath(self.txtTitle).get_attribute('value')
        if currentTitle == expTitle:
            titleCorrect = True
        else:
            self.logInfo("Current TITLE does not match with expected one")
         
        #Check selected option of Category   
        currentCaSelection = Select(driver.find_element_by_xpath(self.ddlCategory))
        currentCategory = currentCaSelection.first_selected_option.text
        if expCategory in currentCategory:
            categoryCorrect = True
        else:
            self.logInfo("Current CATEGORY does not match with expected one")
        
        #Check selected option of Access  
        currentAcSelection = Select(driver.find_element_by_xpath(self.ddlAccess))
        currentAccess = currentAcSelection.first_selected_option.text
        if expAccess == currentAccess:
            accessCorrect = True
        else:
            self.logInfo("Current ACCESS does not match with expected one")
            
        #Check value on 'Article Text' text are
        self.switchToFrame(driver, "jform_articletext_ifr")
        currentText = driver.find_element_by_xpath(self.txtText).get_attribute('textContent')
        driver.switch_to.default_content()
        if expText == currentText:
            textCorrect = True
        else:
            self.logInfo("Current TEXT doesn't not match with expected one")
            
        correctInfomation = titleCorrect and categoryCorrect and accessCorrect and textCorrect
        self.verifyTrue(correctInfomation == True, "\tPASSED : Created %s's information is displayed correctly " %title , "\tFAILED: Created %s's information is NOT displayed correctly " %title)
        
        #Redirect to Manager Article
        option = self.btnToolbarBox.replace("$TOOLBAR BUTTON NAME$", "Close")
        driver.find_element_by_xpath(option).click()
