'''
Created on Dec 15, 2015

@author: van.ngo
'''

import os, sys
import unittest

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


currentPath =  os.path.dirname(os.path.realpath(__file__))
currentPath = currentPath.replace("\\", "/")
modulesPath = str(currentPath)[:str(currentPath).rfind("ABT")]
seleniumPath = modulesPath + "ABT/Libs/selenium"
teamcityPath = modulesPath + "ABT/Libs/teamcity_messages-1.8-py2.7.egg"
print "--" + seleniumPath
print "--" + modulesPath
print "--" + teamcityPath

sys.path.append(modulesPath)
sys.path.append(teamcityPath)
sys.path.append(seleniumPath)



print "--Added"

    
def smokeTestSuite():
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
        
    listTCs = ["test_TC01ArticleCreate","test_TC02ArticleEdit"]
    # Discover and load all unit tests in all files named ``*_test.py`` in ``./src/``   
    path = currentPath.replace("suites","ManagerArticleBU")

    for all_test_suite in unittest.defaultTestLoader.discover(path, pattern='*.py'):
        for test_suite in all_test_suite:
            try:
                for test_case in test_suite:
                    testCaseName = str(str(test_case).split(" (")[0])
                    if testCaseName in listTCs:
                        print "Running TC: " + testCaseName
    #                     suite.addTest(test_case)
                        runner = unittest.TextTestRunner()
                        runner.run(test_case)
    #                     unittest.main(testRunner=runner)
            except Exception, e:
                print str(e)  
if __name__ == '__main__':
    smokeTestSuite()