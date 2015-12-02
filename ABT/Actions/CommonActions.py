'''
Created on Dec 1, 2015

@author: van.ngo
'''
from time import localtime, strftime

from ABT.Interfaces.CommonUI import CommonUI


class CommonActions(CommonUI):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.username = "admin"
        self.password = "admin"
        self.joomlaUrl = "http://192.168.189.207/joomla/administrator/index.php"
        CommonUI.__init__(self)
        
    def logInfo(self, log):
        print strftime("%Y-%m-%d %H:%M:%S: ", localtime()) + log
        
    def logOut(self, driver):
        try:
            driver.find_element_by_xpath(self.lnkLogOut).click()
        except:
            print ("Please log in before logging out")