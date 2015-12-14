'''
Created on Dec 9, 2015

@author: van.ngo
'''

import os
import shutil
from time import strftime, localtime


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)
                
                
if __name__ == '__main__':

    while True:
        time = strftime("%H%M%S", localtime())
        if time == "091000":
            dst = "D:/VanNgo_BackUp_" + time
            copytree("//lgdn-server/LogiGearDN/ES/Anki/BACK UP/Automation Testing/08-19-2014", dst)
            print "run"
            break
