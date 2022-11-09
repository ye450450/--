word=input("단어를 입력하시오. ")
char=input("글자를 입력하시오. ")
count=0
if char in word:
    for i in word:
        count+=1
        if i==char:
            print(char,"는",count,"번째 존재한다")
else:
    print("글자가 존재하지 않습니다.")
