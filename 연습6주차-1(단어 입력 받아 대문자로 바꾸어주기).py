'''
word = input("단어를 입력하시오. ")
length = len(word)
for i in range(length):
    print(word[:i+1])
'''
word = input("단어를 입력하시오. ")
cword= input("바꿀 단어를 입력하시오. ")
index- word.find(cword)
if index==-1:
    print("바꿀 단어가 단어에 없습니다.")
else:
    Bcword=cword.upper()
    word=word.replace(cword,Bcword)
    print(word)
