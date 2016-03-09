# coding=utf-8
'''
Created on Sep 23, 2015

@author: phuong.dang
'''

class AddNewPurchaseRequestPage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.btnDatePickerExpectedDate = "//img[@class = 'ui-datepicker-trigger']"
        self.pickerExpectedDate = "//div[contains(@class, 'ui-datepicker ui-widget') ]"
        self.lblExpectedDay = "//a[contains(@class, 'ui-state-default') and text() ='$Expected_Day$']"
        self.cbxExpectedMonth = "//select[@class = 'ui-datepicker-month']"
        self.cbxExpectedYear = "//select[@class = 'ui-datepicker-year']"
        
        self.cbxRequestType = "//select[@name = 'RequestTypeId']"
        self.cbxDepartment = "//select[@name = 'SubDepartment']"
        self.taJustification = "//textarea[@id = 'Justification']"
        self.rdbBillableToClient = "//input[@name = 'chk_BillableGroup' and @id = '$Billable_To_Client$']"
        self.rdbPaymentMethod = "//label[@hidvalue= '$Payment_Method$']//input"
        self.rdbMoneyType = "//label[@hidvalue= '$Money_Type$']//input"
        self.cbxSalesTax = "//select[@id = 'SaleTaxName']"
        self.cbxResolution = "//select[@id = 'WFResolutionID']"
        self.cbxForwardTo = "//select[@id = 'Assign']"
        self.txtDescription = "//input[@class = 'temp_description']"
        self.btnSave = "//input[@class = 'save']"
        self.msgAddSuccessfully = "//div[@class = 'msgSuccess' and @id = 'systemmessage']"