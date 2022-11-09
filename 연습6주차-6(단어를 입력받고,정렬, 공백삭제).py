#원하는 단어를 입력바독, 알파벳 순서로 정렬, 소문자로 바꾸어 정렬, 공백이 있는 경우 삭제
word = input("단어를 입력하시오. ")
word = word.lower()
word = word.replace(" ","")
print(word)
lword = []
for i in word:
    lword.append(i)
lword.sort()
output=""
for i in lword:
    output+=i
print(output)
'''교수님 방식
word = input("단어를 입력하세요: ")
wordLis =[]
word = word.lower()
for ch in word:
    wordList.append(ch)
print(wordList)

wordList.sort()

while wordList[0] ==' ':
    wordList.remove(" ")

print(wordList)
'''

