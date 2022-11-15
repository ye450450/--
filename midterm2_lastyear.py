#작년 중간고사 기출 - 21900156 김예준

#질문: isalpha()가 되었다가 안되었다가 한다.
# 1번 출력하라고는 안되어있는데 그냥 하나?
#   honor가 왜 3번? // 대,소문자 구분?
# the도 7번 나옴
#프로그램 종료할 때에는 while문 or quit()활용?

import random
import datetime
import sys

word=[] 
capital_word=[] #대문자로 시작하는 단어를 받는 리스트
check = False
while True:
    try:
        if check:
            break
        print("="*5+"Q1 Text from users"+"="*5)
        content=input("Enter text: ")
        print("="*5+"Q2 All words(capital)"+"="*5) #16개
        word=content.split()
        set_word= set(word)
        for i in set_word:
            if i[0].isupper():
                capital_word.append(i)
        print(capital_word, len(capital_word))
        print("="*5+"Q3 All words(mark removed)"+"="*5) #13개
        for unit in capital_word:
            if not unit.isalpha():
                capital_word.remove(unit)
        print(capital_word,len(capital_word))
        capital_word.sort()
        print("="*5+"Q4 words count "+"="*5)
        for i in range(len(capital_word)):
            print(capital_word[i], word.count(capital_word[i]))
        print("="*5+"Q5 random word "+"="*5)
        random_word=random.choice(capital_word)
        print(random_word)
        while True:
            print("="*5+"Q6 user word "+"="*5)
            user_word=input("Enter a word starting... : ")
            if not user_word[0].upper()== random_word[len(random_word)-1].upper():
                print("="*5+"Q7 compiter's win"+"="*5)
                now = datetime.datetime.now()
                print("computer win!!",now.strftime('%Y/%m/%d %H:%M:%S'))
                check=True
                break #프로그램 종료
            random_wordlist=[]
            for unit in capital_word:
                if unit.startswith(user_word[len(user_word)-1].lower()) or unit.startswith(user_word[len(user_word)-1].upper()):
                    random_wordlist.append(unit)
            if len(random_wordlist) == 0:
                print("="*5+"Q9 User's win"+"="*5)
                now = datetime.datetime.now()
                print("user win!!",now.strftime('%Y/%m/%d %H:%M:%S'))
                check=True
                break #프로그램 종료
            else:
                print(random_wordlist)
                print("="*5+"Q8 computer word "+"="*5)
                random_word=random.choice(random_wordlist)
                print(random_word)
                print("="*5+"Q10 Keep Going"+"="*5+"\n")
    except:
        print("="*5+"Q11 Exception Handling"+"="*5)
        print(sys.exc_info()[1],"\n")

