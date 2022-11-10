'''
암호화
s='abcdefghijklmnopqrstuvwxyz'
base_s[]
random.sample(s,26) 사용하여 순서를 바꾸어 알파벳 26개를 base_s에 저장
zip()함수를 사용하여, s와 base_s로 튜플로 이루어진 리스트를 생성
사용자에게 문자열을 입력 받음
각 문자를 튜플의 쌍으로 존재하는 다른 문자로 바꾸어서 출력
'''
import random

s='abcdefghijklmnopqrstuvwxyz'
base_s=[]
base_s=random.sample(s,26)
pair_s=list(zip(s,base_s))
print(pair_s)
password =[] #바뀐 문자들을 받는다.
sentence=input("문자열을 입력하시오.")
for letter in sentence:
    for i in range(26):
        if letter == pair_s[i][0]:
            password.append(pair_s[i][1])
print(password)
