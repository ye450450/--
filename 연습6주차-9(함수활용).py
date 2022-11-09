#문자열의 문자 바꾸어주기

word=input("문자열을 입력하시오. ")
wordlist=word.split(" ")
print(wordlist)
delete=input("제거할 단어를 입력하시오. ")
wordlist.remove(delete)
print(wordlist)
add= input("추가할 단어를 입력하시오. ")
wordlist.append(add)

word=" ".join(wordlist)
print(word)
'''
word=input("문자열을 입력하시오. ")
delete=input("제거할 단어를 입력하시오. ")
add= input("추가할 단어를 입력하시오. ")
word=word.replace(delete,add)
print(word)
'''
