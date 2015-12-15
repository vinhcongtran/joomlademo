'''
Created on Dec 15, 2015

@author: van.ngo
'''
import os, sys
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
if __name__ == '__main__':
    pass