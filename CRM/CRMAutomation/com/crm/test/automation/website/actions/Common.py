# coding=utf-8
'''
Created on Aug 12, 2015

@author: phuong.dang
'''

import datetime
from os.path import os
from time import gmtime, strftime
import time

from pytz import timezone



#####################################################################################
# get current src path on local machine
# Usage : getCurentSrcPath(argument_list)                                                              
# Arguments list:                                                                                        
#                                                                                                                  
#     None
#
# Returns:
#    Current src path
#####################################################################################
def getCurentSrcPath():
    # The current src path will be returned .../overdrive/
    return str(str(os.environ['ANKI_PATH']).replace("\\", "/")).split("overdrive/")[0] + "overdrive/"

#####################################################################################
# Print log with type is info
# Usage : logInfo(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    None
#####################################################################################
def logInfo(log):
    log = getCurrentDateTime() + "\t[INFO]\t" + log
    print log
 
#####################################################################################
# Print log with type is warning
# Usage : logWarning(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    None
#####################################################################################
def logWarning(log):
    # Calculate warnings number
    os.environ['ANKI_WARNINGS'] = str(int(os.environ['ANKI_WARNINGS']) + 1)
    
    log = getCurrentDateTime() + "\t[WARNING]\t" + log
    print log

#####################################################################################
# Print log with type is bug
# Usage : logBug(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    None
#####################################################################################
def logBug(log, number = 1):
    # Calculate warnings number
    for i in range(0, number):
        os.environ['ANKI_WARNINGS'] = str(int(os.environ['ANKI_WARNINGS']) + 1)
    
    log = getCurrentDateTime() + "\t[BUG]\t" + log
    print log

    
#####################################################################################
# Print log with type is fail
# Usage : logFail(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    None
#####################################################################################
def logFail(log, number = 1):
    # Calculate errors number
    for i in range(0, number):
        os.environ['ANKI_ERRORS'] = str(int(os.environ['ANKI_ERRORS']) + 1)
    
    log = getCurrentDateTime() + "\t" + converLogToFail(log)
    print log

    
#####################################################################################
# Convert log to type is fail
# Usage : converLogToFail(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    fail log
#####################################################################################
def converLogToFail(log):
    return "[FAILED]\t " + log
    
#####################################################################################
# Print log with type is pass
# Usage : logPass(argument_list)                                                              
# Arguments list:                                                                                        
#     log 
# Returns:
#    None
#####################################################################################
def logPass(log):
    log = getCurrentDateTime() + "\t[PASSED]\t" + log
    print log
    
#####################################################################################
# Wait for xx seconds
# Usage : wait(argument_list)                                                              
# Arguments list:                                                                                                                                                                                                     
#     seconds: the second time 
# Returns:
#    None
#####################################################################################
def wait(seconds):
    time.sleep(seconds)

#####################################################################################
# Generate a unique value type datetime 
# Usage : generateUniqueValue(argument_list)                                                              
# Arguments list:                                                                                                                                                                                                      
#     None
# Returns:
#    Unique value string
#####################################################################################
def generateUniqueValue():
    return strftime("%Y%m%d%H%M%S", gmtime())

#####################################################################################
# Get current Date time 
# Usage : getCurrentDateTime(argument_list)                                                              
# Arguments list:                                                                                                                                                                                                      
#     None
# Returns:
#    Current GM date time
#####################################################################################
def getCurrentDateTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

#####################################################################################
# Get current Year
# Usage : getCurrentYear(argument_list)                                                              
# Arguments list:                                                                                                                                                                                                        
#     None
# Returns:
#    Current GM Year
#####################################################################################

def getCurrentYear():
    return strftime("%Y", gmtime())

def getCurrentMonth():
    return strftime("%m", gmtime())

def getCurrentDay():
    return strftime("%d", gmtime())

def getAbbreviatedMonthName():
    return strftime("%b", gmtime())

def writeLogFile(logFilePath, value):
    try:
        f = open(logFilePath, 'a+')
        f.writelines(value + "\n")
        f.close()
    except:
        pass
#####################################################################################
# Get EST time 
# Usage : getESTTime(argument_list)                                                              
# Arguments list:                                                                                                                                                                                                     
#     None
# Returns:
#    Current EST time
#####################################################################################
def getESTTime(hoursValue = 0, minutesValue = 0, secondsValue = 0):
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=-4 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%m/%d/%Y %I:%M %p")

def getPSTYear(hoursValue = 0, minutesValue = 0, secondsValue = 0):
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%Y")

def getPSTMonth(hoursValue = 0, minutesValue = 0, secondsValue = 0):
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%b")

def getPSTDate(hoursValue = 0, minutesValue = 0, secondsValue = 0):
    now_utc = datetime.datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    return str(int(now_pacific.strftime("%d")))

def getCETDate():
    now_utc = datetime.datetime.now(timezone('UTC'))
    now_cet = now_utc.astimezone(timezone('Europe/Berlin'))
    return str(int(now_cet.strftime("%d")))

def getGMTDate():
    return str(int(strftime("%d", gmtime())))

def getPSTFullMonth(hoursValue = 0, minutesValue = 0, secondsValue = 0):
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=-7 + hoursValue, minutes=minutesValue, seconds=secondsValue)).strftime("%B")



def convertTimeValueToNumber(timeValue):
    if timeValue != None:
        minuteValue = str(timeValue).split(":")[0]
        secondValue = str(timeValue).split(":")[1]
        num = int(minuteValue) * 60 + int(secondValue)
    else:
        num = -1
    return num