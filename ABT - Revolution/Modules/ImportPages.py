'''
Created on Dec 3, 2015

@author: vinh.cong.tran
'''
from ABT.Actions.Pages.NewArticle import NewArticle
from ABT.Actions.Pages.ControlPanel import ControlPanel
from ABT.Actions.Pages.Login import Login
from ABT.Actions.Pages.ManagerArticle import ManagerArticle
from ABT.Actions.CommonActions import CommonActions

class ImportPages(Login, ControlPanel, CommonActions, NewArticle, ManagerArticle):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Login.__init__(self)
        ControlPanel.__init__(self)
        CommonActions.__init__(self)
        NewArticle.__init__(self)
        ManagerArticle.__init__(self)
