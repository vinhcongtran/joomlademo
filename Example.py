
from time import localtime


pathname = "Content>Article"
# i = 0
# try:
#     i = pathname.find(">")
#     element1 =  pathname[0:i]
#     os.path.split(pathname)
#     

# a = pathname.split(">")
# start = 0
# end = len(a)
# while end > start:
#     print(a[start])
#     start +=1
 
path = "Content>Article Manager>Add New Article" 

i = 0
n = path.count('>')
print n

while n > i:
    x = path.find(">")
    e = path[:x]
    print e

    path = path[x+1:]
    i +=1
    print i
    print path
# words = path.split(">")
# i = 0
# length = len(words)
# print length
# # for each word in the line:
# while i < int(length):
#     for i in length:
#         print words[i]
#         i +=1
        


        
