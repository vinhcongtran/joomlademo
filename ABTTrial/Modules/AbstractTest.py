'''
Created on Dec 12, 2015

@author: vinh.cong.tran
'''
from ABT.Modules.Common.Config import Config

class AbstractTest(Config):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Config.__init__(self)
        
        # Load interface elements and private functions for Control Panel page
        self.controlPanel = FactoryPage.getControlPanel() 
    
        # Load interface elements and private functions for Manager Article page
        self.managerArticle = FactoryPage.getManagerArticle() 
        
        # Load interface elements and private functions for New Article page
        self.newArticle = FactoryPage.getNewArticle() 