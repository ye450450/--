"""
num= int(input("수를 입력하시오. "))
num2= int(input("수를 입력하시오. "))
num3= int(input("수를 입력하시오. "))
mnum= num #가장 먼저 들어온수를 가장 큰수라고 가정한다.
if(mnum<num2):
    mnum=num2
if(mnum<num3):
    mnum=num3
print(mnum)
"""
mnum=0
for i in range(0,3):
    num = int(input("수를 입력하시오. "))
    if(mnum<num):
        mnum=num
print(mnum)
