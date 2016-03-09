# coding=utf-8
'''
Created on Sep 23, 2015

@author: phuong.dang
'''

class HomePage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Assign interface to variables
        self.btnThumbnailByName = "//td[@class = 'chlft']//a[contains(@href, '$THUMBNAIL_NAME$')]"
