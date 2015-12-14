'''
Created on Dec 12, 2015

@author: vinh.cong.tran
'''
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Actions.Pages.NewArticle import NewArticle

class FatoryPage(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def getControlPanel():
        return ControlPanel()
    
    @staticmethod
    def getManagerArticle():
        return ManagerArticle()    
    
    @staticmethod
    def getNewArticle():
        return NewArticle()