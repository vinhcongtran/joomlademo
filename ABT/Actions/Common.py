'''
Created on Dec 1, 2015

@author: van.ngo
'''
from time import localtime, strftime


class Common():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def logInfo(self, log):
        print strftime("%Y-%m-%d %H:%M:%S: ", localtime()) + log
        