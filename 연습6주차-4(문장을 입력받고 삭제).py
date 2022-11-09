#문장을 입력받아서 리스트로 만들어서 출력
#삭제할 문자를 입력받아 그 문자를 생성 된 리스트에서 삭제
#삭제 후 리스트의 내용을 출력
sentence= list(input("문장을 입력하시오 "))
print(sentence)
word= input("삭제할 문자를 입력하시오. ")
for i in sentence:
    if i==word:
        sentence.remove(i)
print(sentence)
