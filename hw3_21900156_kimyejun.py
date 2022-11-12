#hw3 21900156 김예준

#질문 : 읽기 시도한 후에만 파일을 close? -> 오픈한 다음에는 필요없나?

import sys

unique_char=[] #unique한 문자열을 받는 리스트이다.
char_count=[] #문자열이 몇 번 나온지를 받는 리스트이다.
word=[] #단어를 받는 리스트이다.
unique_word=[] #unique한 단어를 받는 리스트이다.
while True:
    try:
        filename=input("Enter the file name to read: ")
        f=open(filename,"r",encoding='utf-8')
        try:
            char=f.read()
            print("Successfully read",len(char),"characters")
            unique_c=set(char)
            print(len(unique_c),"unique characters are found:")
            print(unique_c)
            unique_char=list(unique_c)
            unique_char.sort()
            print("sorted alphabetically in ascending order")
            print(unique_char)
            for i in range(len(unique_char)):
                char_count.append(char.count(unique_char[i]))
            dic_char=dict(zip(unique_char,char_count))
            print("The count of each character :")
            print(dic_char)
            f.close()
            f=open(filename,"r",encoding='utf-8')
            sentence=f.readlines()
            for i in range(len(sentence)):
                word.extend(sentence[i].split())
            unique_word=list(set(word))
            while True:
                while True:
                    input_word=input("Enter at least characters to find words which start with the characters: ")
                    if len(input_word)>=2:
                        break
                search_word=[] #입력받은 문자를 포함하는 단어를 받는 리스트이다.
                for uni_word in unique_word:
                    if uni_word.startswith(input_word):
                        search_word.append(uni_word)
                search_word.sort()
                print(len(search_word),"words are found, which starts with",input_word)
                print(search_word)
                for sear_word in search_word:
                    print(sear_word, "appears", word.count(sear_word),"times in",filename)
                check= input("Do you want to quit? (y) ")
                if check == 'y':
                    break
        except:
            print("error:", sys.exc_info()[1])
            raise
        finally:
            f.close()
            break
    except IOError as err:
        print("{0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[1])
        raise
        
