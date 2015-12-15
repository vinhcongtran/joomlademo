'''
Created on Dec 15, 2015

@author: van.ngo
'''
# Import libs
import os, sys
from time import strftime, localtime
import unittest
import HTMLTestRunner
from teamcity.unittestpy import TeamcityTestRunner

# Add PATH before running
currentPath =  os.path.dirname(os.path.realpath(__file__))
currentPath = currentPath.replace("\\", "/")
modulesPath = str(currentPath)[:str(currentPath).rfind("ABT")]
seleniumPath = modulesPath + "ABT/Libs/selenium"
teamcityPath = modulesPath + "ABT/Libs/teamcity_messages-1.8-py2.7.egg"

sys.path.append(modulesPath)
sys.path.append(teamcityPath)
sys.path.append(seleniumPath)
    
def smokeTestSuite():
    runner = unittest.TextTestRunner()    
    
    #List of test cases wanted to run
    listTCs = ["test_TC01ArticleCreate","test_TC02ArticleEdit"]
    
    # Discover and load all unit tests in all files named ``*_test.py`` in ``./src/``   
    path = currentPath.replace("suites","ManagerArticleBU")

    # Run test cases in the list
    for all_test_suite in unittest.defaultTestLoader.discover(path, pattern='*.py'):
        for test_suite in all_test_suite:
            try:
                for test_case in test_suite:
                    testCaseName = str(test_case)
                    dateTime = strftime("%Y%m%d%H%M%S", localtime())
                    buf = file("D:\\Log\SmokeTestReport" + "_" + dateTime + ".html", "wb")
                    runner = TeamcityTestRunner()
                    runner = HTMLTestRunner.HTMLTestRunner(stream=buf,title=testCaseName + ' - Test Results',description=testCaseName + ' result')
                    runner.run(test_case)
                    if testCaseName in listTCs:
                        print "Running TC: " + testCaseName

                        runner = unittest.TextTestRunner()
                        runner.run(test_case)
            except Exception, e:
                print str(e)  
if __name__ == '__main__':
    smokeTestSuite()