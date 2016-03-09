# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''
from Tkconstants import BROWSE
from hotshot.log import ENTER
import subprocess
import sys
import unittest

from sauceclient import SauceClient
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from com.crm.test.automation.website.actions.Common import *
from com.crm.test.automation.website.module.Config import Config


class AbstractPage(unittest.TestCase, Config):
    browser = None
    
    @classmethod
    def Browser(cls):
        return cls.browser
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        Config.__init__(self)

    ##############################################################################################################
    # Open new browser
    # @param driver: type of browser 
    # @return browser object
    # @author vinh.cong.tran
    ##############################################################################################################
    def openBrowser(self, driver, profile = "normal"):
        try: 

            if AbstractPage.Browser() == None:
                if driver == "Firefox":
                    AbstractPage.browser = webdriver.Firefox()
                        
                   
            logInfo("Open browser successfully")
            AbstractPage.Browser().maximize_window()
            AbstractPage.Browser().set_page_load_timeout(self.cfPageLoadTimeout)
            
            return  AbstractPage.Browser
        except Exception, e:
            print str(e) 
            logWarning("Open browser unsuccessfully")
            # Close Browser and set test case is failed
            self.closeBrowser()
            self.fail()     
    
    ##############################################################################################################
    # Close browser
    # @param none 
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################             
    def closeBrowser(self):
        try:
            AbstractPage.Browser().quit()
            AbstractPage.browser = None
            logInfo("Browser is closed")
        except Exception:
            logWarning("Browser isn't closed")
            
    ##############################################################################################################
    # Clear cache
    # @param none 
    # @return none
    # @author phuong.dang
    ##############################################################################################################             
    def clearCache(self):
        try:
            AbstractPage.Browser().delete_all_cookies()
            logInfo("Browser is cleared cache")
        except Exception:
            logWarning("Browser isn't cleared cache")
    
    ##############################################################################################################
    # Close a latest window
    # @param none 
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def closeALatestWindow(self):
        try:
            currentwindows = AbstractPage.Browser().window_handles
            if len(currentwindows) > 1:
                AbstractPage.Browser().close()
        except Exception, e:
            logInfo(str(e))
             
    ##############################################################################################################
    # Navigate to a url and handle the Get Up To Speed popup
    # @param url: Url path
    # @param driver: Type of browser
    # @return browser object
    # @author vinh.cong.tran
    ##############################################################################################################         
    def navigateToWeb(self, url, driver):
        try:
            # Handle open browser if didn't started
            self.openBrowser(driver)
            
            # The default time for wait an element
            AbstractPage.Browser().implicitly_wait(self.cfImplicitlyTimeWait)
            
            AbstractPage.Browser().get(url)
            
            logInfo("Navigate to %s successfully" % url)
            return AbstractPage.Browser()
        except Exception, e:
            print str(e)
            logWarning("Navigate to %s unsuccessfully" % url)
            # Close Browser and set test case is failed
            self.closeBrowser()
            self.fail()
           
    
    ##############################################################################################################
    # Get element of a browser by xpath
    # @param xPathPath: the xpath of element
    # @return element
    # @author vinh.cong.tran
    ##############################################################################################################
    def getElementByXPath(self, xPathPath, timeout = Config().cfShortTime, isBug = False):
        element = None
        try:
            # First, set default time for wait an element
            AbstractPage.Browser().implicitly_wait(self.cfImplicitlyTimeWait)
            
            if timeout != 0:
                # Set new time value for wait an element
                AbstractPage.Browser().implicitly_wait(timeout)
            
            # Get element by xpath
            element = AbstractPage.Browser().find_element_by_xpath(xPathPath)
            
            return element
        
        except Exception:
            if isBug == False:
                # Close Browser and set test case is failed
                logWarning("Cannot get element with xpath: " + xPathPath)
                self.closeBrowser()
                self.fail()
                
        return None
        
    ##############################################################################################################
    # Does element is exist by xpath
    # @param xPathPath: the xpath of element
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def doesElementExisted(self,element_xpath, timeout = Config().cfShortTime):
        try:
            WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: self.getElementByXPath(element_xpath, timeout, True))
            return True
        except Exception:
            return False
        
    ##############################################################################################################
    # Does element is not exist by xpath
    # @param xPathPath: the xpath of element
    # @return True/False
    # @author vuong.vo
    ##############################################################################################################             
    def doesElementNotExisted(self,element_xpath, timeout = 10):
        try:
            WebDriverWait(AbstractPage.Browser, timeout).until_not(lambda driver: self.getElementByXPath(element_xpath, timeout, True))
            return True
        except Exception:
            return False

    ##############################################################################################################
    # Click on an element by xpath
    # @param xPathPath: the xpath of element
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def click(self, xPathPath, isBug = False):
        element = self.getElementByXPath(xPathPath, isBug = isBug)       

        if element != None:
            element.click()
        else:
            logWarning("Cannot click on control with xpath: " + xPathPath)
                      
    ##############################################################################################################
    # verify True expression
    # @param expression: True/False
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyTrue(self, expression, passMsg, failMsg):
        try:
            if expression == True:
                logPass(passMsg)
 
            self.assertTrue(expression, failMsg)
        
        except AssertionError, e:
            logFail(str(e))
    
    ##############################################################################################################
    # verify In
    # @param member: The value want to check in container
    # @param container: The container value
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyIn(self, member, container, passMsg, failMsg):
        try:
            if member in container:
                logPass(passMsg)
 
            self.assertIn(member, container, failMsg)
                 
        except Exception, e:
            logFail(str(e))
    ##############################################################################################################
    # verify Not In
    # @param member: The value want to check not in container
    # @param container: The container value
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author tam.van.nguyen
    ##############################################################################################################
    def verifyNotIn(self, member, container, passMsg, failMsg):
        try:
            if member not in container:
                logPass(passMsg)
 
            self.assertNotIn(member, container, failMsg)
                 
        except Exception, e:
            logFail(str(e))
    ##############################################################################################################
    # verify Equal expression
    # @param first: first value
    # @param second: second value
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyEqual(self, first, second, passMsg, failMsg):
        try:
            if first == second:
                logPass(passMsg)
                
            self.assertEqual(first, second, failMsg)
                
        except Exception, e:
            logFail(str(e))
            
    ##############################################################################################################
    # verify Equal expression
    # @param first: first value
    # @param second: second value
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vuong.vo
    ##############################################################################################################
    def verifyNotEqual(self, first, second, passMsg, failMsg):
        try:
            if first != second:
                logPass(passMsg)
            
            self.assertNotEqual(first, second, failMsg)
                
        except Exception, e:
            logFail(str(e))
    
    ##############################################################################################################
    # verify False expression
    # @param expression: True/False
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyFalse(self, expression, passMsg, failMsg):
        try:
            if expression == False:
                logPass(passMsg)
 
            self.assertFalse(expression, failMsg)
                
        except Exception, e:
            logFail(str(e))
    
    ##############################################################################################################
    # verify Is expression
    # @param expr1: Value 1
    # @param expr2: Value 2
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyIs(self, expr1, expr2, passMsg, failMsg):
        try:
            if expr1 is expr2:
                logPass(passMsg)
 
            self.assertIs(expr1, expr2, failMsg)
                
        except Exception, e:
            logFail(str(e))
    
    ##############################################################################################################
    # verify multi line equal
    # @param expr1: Value 1
    # @param expr2: Value 2
    # @param passMsg: Pass message
    # @param failMsg: Fail message
    # @author vinh.cong.tran
    ##############################################################################################################
    def verifyMultiLineEqual(self, first, second, passMsg, failMsg):
        try:
            if first == second:
                logPass(passMsg)
 
            self.assertMultiLineEqual(first, second, failMsg)
                
        except Exception, e:
            logFail(str(e))
                    
    ##############################################################################################################
    # get current url of browser
    # @return current url 
    # @author vinh.cong.tran
    ##############################################################################################################
    def getCurrentUrl(self):
        try:
            currentUrl = ""
            currentUrl = AbstractPage.browser.current_url
        except Exception, e:
            logWarning(str(e))
            
        return currentUrl
    
    ##############################################################################################################
    # Click on an element by xpath and switch to new window after clicking on it
    # @param xPathPath: the xpath of element
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def clickAndSwitchWindow(self, xPathPath):
        try:
            currentwindows = AbstractPage.Browser().window_handles
            element = self.getElementByXPath(xPathPath)
            element.click()
            time.sleep(3)
            newwindows = AbstractPage.Browser().window_handles # 1 extra window shows up here.
            
            newwindow = list(set(newwindows) - set(currentwindows))[0]
            # Put focus on current window which will, in fact, put focus on the current visible tab
            AbstractPage.Browser().switch_to_window(newwindow)
            AbstractPage.Browser().maximize_window()

        except Exception, e:
            print str(e)
            logWarning("Cannot click and switch to new window with control " + xPathPath)
    
    ##############################################################################################################
    # Switches focus to the specified frame, by index, name, or webelement.
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def switchToFrame(self, frameReference, index = 0):
        try:
            if self.cfDriver == "Chrome" or self.cfDriver == "Ie":    
                AbstractPage.Browser().switch_to_frame(index)
            elif self.cfDriver == "Firefox":
                AbstractPage.Browser().switch_to_frame(frameReference)
        except Exception, e:
            print e
            logWarning("Cannot switch to frame " + frameReference)
    
    ##############################################################################################################
    # Switches focus to the specified frame, by index, name, or webelement.
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def switchToDefaultContent(self):
        try:
            AbstractPage.Browser().switch_to_default_content()
        except Exception:
            logWarning("Cannot switch to default content")

    ##############################################################################################################
    # Get element property value by xpath
    # @param element_xpath: the xpath of element
    # @param propertyName: name of property want to get  
    # @return value of property name
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getElementProperty(self,element_xpath, propertyName, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            
            if element != None:
                return element.get_attribute(propertyName)
            else:
                logWarning("Cannot get property '"+ propertyName +"' of control with xpath '"+ element_xpath +"'")
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Set checkbox status
    # @param element_xpath: the xpath of element
    # @param status: True/False  
    # @return value of property name
    # @author vinh.cong.tran
    ##############################################################################################################             
    def setCheckboxStatus(self,element_xpath, status = False):
        try:
            isSelected = self.getElementProperty(element_xpath, "checked")
            if (isSelected == None):
                isSelected = False
            
            if isSelected != status:
                self.click(element_xpath)
            
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Get element text by xpath
    # @param element_xpath: the xpath of element
    # @return value of property name
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getElementText(self,element_xpath, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            if element != None:
                return element.text
            else:
                logWarning("Cannot get text of control with xpath '"+ element_xpath +"'")
        except Exception, e:
            logWarning(str(e))

        return None
        
    ##############################################################################################################
    # Wait for an element is exists
    # @param xPathPath: the xpath of element
    # @return None
    # @author vinh.cong.tran
    ##############################################################################################################             
    def waitForElementExisted(self,element_xpath, timeout = 30):
        try:
            
            WebDriverWait(AbstractPage.Browser, timeout).until(lambda driver: self.getElementByXPath(element_xpath, timeout))
        except Exception:
            logWarning("Control with xpath: %s is not existed" % element_xpath)
    
    ##############################################################################################################
    # click element at position
    # @param element_xpath: the xpath of element
    # @param x: The x position
    # @param y: The y position
    # @author vinh.cong.tran
    ##############################################################################################################
    def clickAt(self, element_xpath, x, y):
        try:
            ActionChains(AbstractPage.Browser()).move_to_element(self.getElementByXPath(element_xpath)).move_by_offset(x, y).click().perform()
        except Exception, e:
            logInfo(str(e))
            logWarning("Cannot click on control with xpath: " + element_xpath + " at position ("+str(x) + "," + str(y) + ")")
    
    ##############################################################################################################
    # Hover element 
    # @param element_xpath: the xpath of element
    # @author tam.van.nguyen
    ##############################################################################################################
    def hoverMouse(self, element_xpath):
        try:
            element = self.getElementByXPath(element_xpath)
            if element != None:
                    heighElement = 0
                    if element.location["y"] >= 200:
                        heighElement = element.location["y"] - 150
                    AbstractPage.Browser().execute_script("window.scrollTo(0, " + str(heighElement) + ");")
                    # Wait for 0.5 second to make sure script is run stable
                    wait(0.5)
                        
                    ActionChains(AbstractPage.Browser()).move_to_element(self.getElementByXPath(element_xpath)).move_by_offset(1, 1).perform()
            else:
                logWarning("Cannot find control with xpath: " + element_xpath)
        except Exception, e:
            logInfo(str(e))
            logWarning("Cannot find control with xpath: " + element_xpath + ")")
       
    ##############################################################################################################
    # Go back
    # @author vinh.cong.tran
    ##############################################################################################################        
    def goBack(self):
        self.browser.back()
        # Handle with ChromeDrive
        if self.cfDriver == "Chrome":
            wait(3)
    
    ##############################################################################################################
    # Refresh the current page
    # @author vinh.cong.tran
    ##############################################################################################################        
    def refresh(self):
        self.browser.refresh()
        
    ##############################################################################################################
    # Press Enter key
    # @author vuong.vo
    ##############################################################################################################        
    def pressEnterKey(self, element_xpath, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            if element != None:
                element.send_keys(Keys.ENTER)
            else:
                logWarning("Cannot presses enter key into control with xpath: " + element_xpath)
        except Exception, e:
            logWarning(str(e))
        
    ##############################################################################################################
    # Enter value into element
    # @param xPathPath: the xpath of element
    # @param value: The value want enter
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def enter(self, xPathPath, value, isBug = False):
        try:
            element = self.getElementByXPath(xPathPath, isBug)
            
            if element != None:
                element.clear()
                try:
                    element.send_keys(str(value))
                except:
                    element.send_keys(value)
            else:
                logWarning("Cannot enter value '"+ str(value) +"' into control with xpath: " + xPathPath)
        except Exception, e:
            logWarning(str(e))
    
    ##############################################################################################################
    # Wait for an element is not exists
    # @param xPathPath: the xpath of element
    # @return None
    # @author vinh.cong.tran
    ##############################################################################################################             
    def waitForElementNotExisted(self,element_xpath, timeout = 30):
        try:
            elementExist = True
            # Loop to wait for element not exists
            for i in range(0,timeout):
                elementExist = self.doesElementExisted(element_xpath, 1)
                if elementExist == False:
                    break
                else:
                    i =i+1
                    wait(1)
            
            if elementExist == True:
                logWarning("Control with xpath: %s is existed" % element_xpath)
                
        except Exception:
            logWarning("Control with xpath: %s is not existed" % element_xpath)
    
    ##############################################################################################################
    # Move to element by xpath
    # @param xPathPath: the xpath of element
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def moveToElement(self, xPathPath):
        try:
            wait(1)
            actions = ActionChains(self.browser)
            actions.move_to_element(self.getElementByXPath(xPathPath))
            actions.perform()
        except Exception, e:
            logWarning(str(e))
            logWarning("Cannot move to control with xpath: " + xPathPath )
    
    ##############################################################################################################
    # Focus to an element
    # @param xPathPath: the xpath of element
    # @return None
    # @author vinh.cong.tran
    ##############################################################################################################             
    def focusElement(self,element_xpath):
        try:
            self.enter(element_xpath, None)
        except Exception:
            logWarning("Cannot focus to control with xpath: %s" % element_xpath)
    
    ##############################################################################################################
    # Select an item in dropdown by text
    # @param xPathPath: the xpath of dropdown
    # @param value: the value want select
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def selectItemByText(self, xPathPath, itemValue, isBug = False):
        try:
            item = self.getElementByXPath(xPathPath, isBug)
            if item != None:
                select = Select(item)
                select.select_by_visible_text(str(itemValue))

            else:
                logWarning("Cannot select item '" + str(itemValue) + "' in dropdown list with XPath: '" + str(xPathPath) + "'")
        except Exception, e:
            logWarning(str(e))

    ##############################################################################################################
    # Select an item in dropdown by value
    # @param xPathPath: the xpath of dropdown
    # @param value: the value want select
    # @return none
    # @author tam.van.nguyen
    ##############################################################################################################
    def selectItemByValue(self, xPathPath, value, isBug = False):
        try:
            item = self.getElementByXPath(xPathPath, isBug)
            if item != None:
                select = Select(item)
                select.select_by_value(value)
            else:
                logWarning("Cannot select item '" + str(value) + "' in dropdown list with XPath: '" + str(xPathPath) + "'")
                
        except Exception, e:
            logWarning(str(e))
    
    ##############################################################################################################
    # Select an item in dropdown by index
    # @param xPathPath: the xpath of dropdown
    # @param value: the value want select
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def selectItemByIndex(self, xPathPath, itemIndex, isBug = False):
        try:
            item = self.getElementByXPath(xPathPath, isBug)
            if item != None:
                select = Select(item)
                select.select_by_index(itemIndex)
            else:
                logWarning("Cannot select item index '" + str(itemIndex) + "' in dropdown list with XPath: '" + str(xPathPath) + "'")
        except Exception, e:
            logWarning(str(e))
    
    ##############################################################################################################
    # Get value of css property of element
    # @param element_xpath: the xpath of element
    # @param cssPropertyName: css property want to get value
    # @return value of css property
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getValueOfCssProperty(self,element_xpath, cssPropertyName, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            if element != None:
                return element.value_of_css_property(cssPropertyName)
            else:
                logWarning("Cannot get css property name '" + str(cssPropertyName) + "' in with XPath: '" + str(element_xpath) + "'")
                
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Get element text by xpath
    # @param element_xpath: the xpath of element
    # @return value of property name
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getDropdownListCurrentText(self,element_xpath, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            
            if element != None:
                select = Select(element)
                selOption = select.first_selected_option
               
                return selOption.text
            else:
                logWarning("Cannot get the current text of dropdown list with XPath: '" + str(element_xpath) + "'")
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Get current status of checkbox
    # @param element_xpath: the xpath of element
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getCheckboxStatus(self,element_xpath, isBug = False):
        try:
            element = self.getElementByXPath(element_xpath, isBug)
            if element != None:
                return element.is_selected()
            else:
                logWarning("Cannot get the status of checkbox with XPath: '" + str(element_xpath) + "'")
        
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Get the number of element by xpath
    # @param element_xpath: the xpath of element
    # @return Number of elements
    # @author vinh.cong.tran
    ##############################################################################################################             
    def getNumberOfElement(self,element_xpath):
        try:
            element = self.Browser().find_elements_by_xpath(element_xpath)
            
            if element != None:
                return len(element)
            else:
                logWarning("Cannot get the number of element have XPath are: '" + str(element_xpath) + "'")
        
        except Exception, e:
            logWarning(str(e))
        
        return None
    
    ##############################################################################################################
    # Switch to the latest window
    # @author vinh.cong.tran
    ##############################################################################################################
    def switchToLatestWindow(self):
        wait(1)
        if self.Browser() != None:
            self.Browser().switch_to_window(self.Browser().window_handles[-1])
    
    ##############################################################################################################
    # Use Sendkey enter to click on an element by xpath
    # @param xPathPath: the xpath of element
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def clickByEnter(self, xPathPath, isBug = False):
        try:
            element = self.getElementByXPath(xPathPath, isBug)
            
            if element != None:
                element.send_keys(Keys.ENTER)
            else:
                logWarning("Cannot click by using enter with element has XPath: '" + str(xPathPath) + "'")
                
        except Exception, e:
            logInfo(str(e))
            
    ##############################################################################################################
    # Get selected item value of dropdown list
    # @param xPathPath: the xpath of dropdown
    # @return item value
    # @author vinh.cong.tran
    ##############################################################################################################
    def getSelectedItemValue(self, xPathPath, isBug = False):
        try:
            element = self.getElementByXPath(xPathPath, isBug)
            if element != None:
                select = Select(element)
                return select.first_selected_option.text
            else:
                logWarning("Cannot get selected item value of dropdown list has xpath: " + xPathPath)
        except Exception, e:
            logInfo(str(e))
            
    ##############################################################################################################
    # Does an element is displayed under another element by xpath
    # @param element_xpath: the xpath of element want to check
    # @param another_element_xpath: the xpath of another element want to check
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def doesAControlUnderAnotherControl(self,element_xpath, another_element_xpath, timeout = 10):
        try:
            firstElementExist = self.doesElementExisted(element_xpath, timeout)
            secondElementExist = self.doesElementExisted(another_element_xpath, timeout)
             
            if (firstElementExist == True) and (secondElementExist == True):
                firstElement = self.getElementByXPath(element_xpath, timeout)
                secondElement = self.getElementByXPath(another_element_xpath, timeout)
                
                if firstElement.location["y"] > secondElement.location["y"]:
                    return True

        except Exception, e:
            logInfo(str(e))
        
        return False
    
    ##############################################################################################################
    # Does an element is displayed above another element by xpath
    # @param element_xpath: the xpath of element want to check
    # @param another_element_xpath: the xpath of another element want to check
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def doesAControlAboveAnotherControl(self,element_xpath, another_element_xpath, timeout = 10):
        try:
            firstElementExist = self.doesElementExisted(element_xpath, timeout)
            secondElementExist = self.doesElementExisted(another_element_xpath, timeout)
             
            if (firstElementExist == True) and (secondElementExist == True):
                firstElement = self.getElementByXPath(element_xpath, timeout)
                secondElement = self.getElementByXPath(another_element_xpath, timeout)
                
                if firstElement.location["y"] < secondElement.location["y"]:
                    return True
            return False
        
        except Exception, e:
            logInfo(str(e))
    
    ##############################################################################################################
    # Does an element is displayed next to another element by xpath
    # @param element_xpath: the xpath of element want to check
    # @param another_element_xpath: the xpath of another element want to check
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def doesAControlNextToAnotherControl(self,element_xpath, another_element_xpath, timeout = 10):
        try:
            firstElementExist = self.doesElementExisted(element_xpath, timeout)
            secondElementExist = self.doesElementExisted(another_element_xpath, timeout)
             
            if (firstElementExist == True) and (secondElementExist == True):
                firstElement = self.getElementByXPath(element_xpath, timeout)
                secondElement = self.getElementByXPath(another_element_xpath, timeout)
                
                if firstElement.location["x"] < secondElement.location["x"]:
                    return True
            return False
        
        except Exception, e:
            logInfo(str(e))
    
    ##############################################################################################################
    # Does an element is displayed at the right of the page
    # @param element_xpath: the xpath of element want to check
    # @return True/False
    # @author tam.van.nguyen
    ##############################################################################################################             
    def doesAnElementDisplayAtTheRightOfPage(self,element_xpath, timeout = 10):
        try:
            elementExist = self.doesElementExisted(element_xpath, timeout)
            if (elementExist == True):
                firstElement = self.getElementByXPath(element_xpath, timeout)
                dicti = self.Browser().get_window_size()
                pageWidth = float(dicti['width'])
                elementWidth = float(firstElement.location["x"])
                if pageWidth/2 < elementWidth:
                    return True
            return False
        
        except Exception, e:
            logInfo(str(e))
            
    ##############################################################################################################
    # Does an image exists using Sikuli lib
    # @param image_path: the image path
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################             
    def doesImageExists(self, image_path):
        try:
            # Update the path file
            fullImagePath = str(os.path.dirname(os.path.realpath(__file__))).replace("actions","interfaces\\images") + image_path
            sikuliActionPath = str(os.path.dirname(os.path.realpath(__file__))) + "\\sikuli\\doesImageExist.sikuli"
            commandLine = "call \"" + self.cfSikuliIDEPathFile + "\" -r \"" + sikuliActionPath +"\" \"" + fullImagePath + "\""
            
            # Run command
            p = subprocess.Popen(commandLine, shell=True, stdout = subprocess.PIPE)
            stdout, stderr = p.communicate()
            
            if "Match" in str(stdout):
                return True
            return False
        
        except Exception, e:
            logInfo(str(e))
    
    ##############################################################################################################
    # Wait for page loaded by using javascript
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################
    def waitForPageLoadedByUsingJavascript(self):
        pageLoaded = ""
        count = 0
        while (pageLoaded != "complete" and count <= self.cfPageLoadTimeout):
            wait(0.5)
            pageLoaded = AbstractPage.Browser().execute_script("return document.readyState")
            count = count + 1
        
        if (count > self.cfPageLoadTimeout):
            logWarning("Page isn't loaded completely ịn " + str(self.cfPageLoadTimeout) + " seconds")
            # Close Browser and set test case is failed
            self.closeBrowser()
            self.fail()
    
    ##############################################################################################################
    # Click on an element with xpath by using Javascript
    # @param xPathPath: the xpath of element
    # @return none
    # @author vinh.cong.tran
    ##############################################################################################################
    def clickByUsingJavascript(self, xPathPath, isBug = False, moveMouse = True):           
        element = self.getElementByXPath(xPathPath, isBug = isBug)       

        if element != None:
            if self.cfDriver == "Chrome":
                if moveMouse == True:
                    heighElement = 0
                    if element.location["y"] >= 200:
                        heighElement = element.location["y"] - 150
                    AbstractPage.Browser().execute_script("window.scrollTo(0, " + str(heighElement) + ");")
                
            executeScript = "document.evaluate(\"" + xPathPath + "\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();"
            self.Browser().execute_script(executeScript)
            
            # Handle issue webdriver is performing the action on webelement while page is getting loaded
            self.waitForPageLoadedByUsingJavascript()
            
        else:
            logWarning("Cannot click on control with xpath: " + xPathPath)
            
    ##############################################################################################################
    # Does element cursor focus
    # @return True/False
    # @author vinh.cong.tran
    ##############################################################################################################
    def doesElementCursorFocus(self, element_xPath, isBug = False):
        try:
            element = self.getElementByXPath(element_xPath)
            focusElement = AbstractPage.Browser().switch_to_active_element()
            element.get_attribute("id")
            focusElement.get_attribute("id")
            if element == focusElement:
                return True
            elif element != focusElement:
                return False
        except Exception, e:
            logInfo(str(e))
            
    ##############################################################################################################
    # Does element display
    # @return none
    # @author phuong.dang
    ##############################################################################################################
    def doesElementDisplay(self, element_xPath, timeout = Config().cfShortTime):
        try:
            element = self.getElementByXPath(element_xPath, timeout, True)
            status = element.is_displayed()
            return status
        except Exception, e:
#             logInfo(str(e))
            return None
            
    ##############################################################################################################
    # Clear data in field
    # @return none
    # @author phuong.dang
    ##############################################################################################################
    def clearDataOnField(self, element_xPath):
        try:
            element = self.getElementByXPath(element_xPath)
            element.clear()
        except Exception, e:
            logInfo(str(e))
            
    ##############################################################################################################
    # Scroll to element
    # @return none
    # @author phuong.dang
    ##############################################################################################################
    def scrollToElement(self, element_xPath):
        try:
            element = self.getElementByXPath(element_xPath)
            if element != None:
                heighElement = 0
                if element.location["y"] >= 200:
                    heighElement = element.location["y"] - 150
                AbstractPage.Browser().execute_script("window.scrollTo(0, " + str(heighElement) + ");")
        except Exception, e:
            logInfo(str(e))
        