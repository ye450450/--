import string

sentence= input("30글자 이상의 영어문장을 입력하시오. ")
countA=0
countUp=0
countLow=0
for i in sentence:
    if i.isalpha():
        countA+=1
    if i.isupper():
        countUp+=1
    if i.islower():
        countLow+=1
    
print(countA, countUp, countLow)

"""
for i int sentence:
    countA+=i.isalpha()
    countUp+=i.isupper()
    countLow+=i.islower()
"""
