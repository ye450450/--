word = input("단어를 입력하시오 ")
output =""
countUp=0
countLow=0
countNo=0
for i in word:
    if i.islower():
        output+=i.upper()
        countLow+=1
    elif i.isupper():
        output+=i.lower()
        countUp+=1
    else:
        output+=i
        countNo+=1
print(output)
print("대문자",countUp)
print("소문자",countLow)
print("대소문자가 아닌 문자",countNo)
