'''
Created on Dec 17, 2015

Need Libraries : xlrd, xlsxwriter, JIRA. They will be found at 

@author: van.ngo
'''
import xlrd
import  xlsxwriter
from jira.client import JIRA
from jira.resources import Priority
import re



######################################################################################
# Usage: Open a file                                                            
# Arguments list: path of the file expecting to open                                                                                        
# Return: a list of all data in the open file 
#####################################################################################
def openFile(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
    listData = list()
    first_sheet = book.sheet_by_index(0)
    for sheet in book.sheets():
        for row in range(sheet.nrows):
            if row >= 10:
                listData.append(first_sheet.row_slice(row,0,sheet.ncols))
    return listData


######################################################################################
# Usage: Get the bug list including Jira ID from the Bug Tracking file                                                         
# Arguments list: Path containing Bug Tracking file                                                                                       
# Return: a list including Jira ID
#####################################################################################
def getJiraIDListFromBugTrackingFile(path): 
    listData = openFile(path)       
    jirasList = list()
    row =10
    print len(listData)
    for row in range(len(listData)):
        issueString = str(listData[row][1])
        issue = issueString[7:len(issueString)-1]
        jirasList.append(issue)
    print jirasList
    return jirasList


######################################################################################
# Usage: Write data on an excel file                                                            
# Arguments list:
#         path: expected path to save the file
#         excelJiraList: a list of Bug ID 
#         priorityList: a list of priority bugs
#         statusList: a list of status bugs
#         resolutionList: a list of resolution bugs
#####################################################################################
def writeFile(path, excelJiraList, priorityList, statusList, resolutionList):
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet("Bug List")
    
    bold = workbook.add_format({'bold': 1})
    worksheet.write('A1', 'Jira ID', bold)
    worksheet.write('B1', 'Priority', bold)
    worksheet.write('C1', 'Status', bold)
    worksheet.write('D1', 'Resolution', bold)

    row = 1
    #Write the latest information into new Excel file
    print 'length : ' + str(len(excelJiraList))
    for i in range(0, len(excelJiraList)):
        print str(excelJiraList[i])+ "," + str(priorityList[i]) + "," + str(statusList[i])+ "," +  str(resolutionList[i])
        worksheet.write(row, 0, str(excelJiraList[i]))
        worksheet.write(row, 1, priorityList[i])
        worksheet.write(row, 2, str(statusList[i]))
        worksheet.write(row, 3, str(resolutionList[i]))
        row = row+1

 
######################################################################################
# Usage: Get the latest priority, resolution, status of a list bug from Jira                                                            
# Argument: a list of issues
# Return: the latest priority, resolution, status of a list bug from Jira
#####################################################################################
def getBugInfo(issues):
    
    options = {'server': 'https://ankiinc.atlassian.net/'}
    try:
        jira = JIRA(options, basic_auth=('van.ngo@logigear.com', 'L0gigear'))
        priorityList= list()
        statusList= list()
        resolutionList= list()
    
        #Get all information from Jira based on excel bug list
            
        for i, issue in enumerate(issues):
            
            try:
                l = len(issue)
                m = re.search('^OD-\d*$', issue.strip())
                if m != None:
                    issue = jira.issue(issue.strip())
                    #Get status of all bugs in the excel list
                    statusList[len(statusList):] = [issue.fields.status]
                 
                    #Get Resolution of all bugs in the excel list
                    resolutionList[len(resolutionList):] = [issue.fields.resolution]
                
                    #Get priority of all bugs in the excel list
                    priorityList[len(priorityList):] = [issue.fields.priority.name]
                
                else:
                    print "Issue at " + str(i + 1) +" is NOT an ID bug" 
                    statusList[len(statusList):] = "N"
                    resolutionList[len(resolutionList):] = "N"
                    priorityList[len(priorityList):] = "N"
                
            except:
                print "Warning : issue : " + str(issue) + " , index: " + str(i)
        
        
        print statusList
        return statusList,resolutionList,priorityList
    except Exception as e:
        jira = None
        print e
  
    


#----------------------------------------------------------------------
if __name__ == "__main__":
    
    path = "\\\\lgdn-server\\LogiGearDN\\ES\\Anki\\04. DELIVERABLES\\Manual Testing\\Working\\Bug List\\Anki OverDrive\\iOS-AnkiOverDrive-Bugs Tracking.xlsx"
    excelJiraList = getJiraIDListFromBugTrackingFile(path)
    statusList,resolutionList,priorityList = list(getBugInfo(excelJiraList))
    writeFile('E:\\iOS_AnkiOverDrive_Bugs_Tracking_Update.xlsx', excelJiraList, priorityList, statusList, resolutionList)
