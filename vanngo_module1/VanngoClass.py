'''
Created on Nov 25, 2015

@author: van.ngo
'''
import unittest


class MyClass():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def ptb2( self, a, b, c):
        return a + b + c 
    
    
    if __name__ == '__main__':
        ptb2(2, 2, 2)
        runner = HTMLTestRunner.HTMLTestRunner(
                                stream=buf,
                                title=testcase + 'Exercise 03 - Test Results',
                                description=testcase + ' result'
                                )
   
   
    #     suite = unittest.TestLoader().loadTestsFromTestCase(Ex03Article)
#     for testcase in tests:
#         suite = unittest.TestSuite()
#         suite.addTest(Ex03Article(testcase))
#         
#     dateTimeStamp = strftime("%Y%m%d %H%M%S", localtime())
#     buf = file("D:\\Log\EX03TestReport" + "_" + dateTimeStamp + ".html", "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=buf, title=testcase + 'Exercise 03 - Test Results', description=testcase + ' result')
#     runner = TextTestRunner()
#     runner.run(suite)




# #     for testcase  in tests:
#         suite = unittest.TestLoader().loadTestsFromTestCase(Ex02Article)
# #         suite = unittest.TestSuite()
# #         suite.addTest(Ex02Article(testcase))
#         buf = file("D:\\Log\EX02TestReport" + "_" + dateTime + ".html", "wb")
#         runner = HTMLTestRunner.HTMLTestRunner(
#                         stream=buf,
#                         title=testcase + ' Ex02 - Test Results',
#                         description=testcase + ' result'
#                         )
#     
#     runner.run(suite)
