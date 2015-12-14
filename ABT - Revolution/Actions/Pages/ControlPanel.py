'''
Created on Dec 1, 2015

@author: van.ngo
'''
from selenium.webdriver.common.action_chains import ActionChains

from ABT.Interfaces.ControlPanelPage import ControlPanelPage


class ControlPanel(ControlPanelPage):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ControlPanelPage.__init__(self)

    
    def checkPageExist(self, driver):
        try:
            driver.find_element_by_xpath(self.pagUnique)
            print "The Control Panel page is displayed"
        except:
            print "The Control Panel page isn't displayed"
            
    ##############################################################################################################
    # Navigate to a page by clicking on a menu item
    # @param driver: type of browser
    # @param path: path of menu item, menu items separates to each other by '>' (e.g.: Content>Article Manager)
    ##############################################################################################################       
    def navigateMenu(self, driver, path):
        i = 0
        n = path.count(">")
        while n > i:
            x = path.find(">")
            e = path[:x]
            node = driver.find_element_by_xpath("//div[@id = 'module-menu']//a[text() = '" + e + "']")
            ActionChains(driver).move_to_element(node).perform()
        
            path = path[x+1:]
            i +=1
            if i == n:
                node = driver.find_element_by_xpath("//div[@id = 'module-menu']//a[text() = '" + path + "']")
                node.click()
                
        
        