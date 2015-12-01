'''
Created on Dec 1, 2015

@author: van.ngo
'''


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from ABT.Actions.Common import Common
from ABT.Actions.Pages.ControlPanel import ControlPanel
from ABT.Actions.Pages.Login import Login


class ActicleBU(Login, ControlPanel, Common):
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
    
    
    def TC01(self):
        # Main steps
        # Open browser
        browser = self.openBrowser()
        
        self.logInfo("Step 1 - Navigate to Joomla administrator admin page")
        self.navigate(browser, "http://192.168.189.207/joomla/administrator/index.php")
        
        self.logInfo("Step 2,3,4 - Log In an existing account")
        self.login(browser, "admin", "admin")
        
        #Step 5: Select Content > Article Manager
        self.logInfo("Step 5 - Select Content > Article Manager")
        self.navigateMenu(browser, "Content>Article Manager")

        
        #VP: Control Panel page displays
#         self.checkPageExist(browser)
        
if __name__ == '__main__':
    ActicleBU().TC01()