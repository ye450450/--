'''
from copy import *

numlist=[0,1,2,3,4]
numshallow=numlist
numdeep=deepcopy(numlist)
numlist.append(5)
numdeep.append(6)
print(numlist,"//",numshallow,"//",numdeep)
'''
word =list(input("단어를 입력하시오. "))
output= " ".join(word)
print(output)
