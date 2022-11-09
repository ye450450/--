import random

test_txt ="암호화 암호화 하려는 텍스트에서 고유 문자들을 뽑아낸다.고유 문자들의 개수만큼 랜덤 숫자를 만든다.고유 문자를 key로 하고 랜덤 숫자를 value로 하는 dictionary를 만든다.이것이 암호화에 사용되는 secret code 가 된다.텍스트를 secret code를 이용하여 랜덤 숫자들의 나열로 암호화한다.복호화reverse secret code를 만든다. 암호화 할 때 사용했던 secret code 에서 value를 가져와서 key로 하고, key를 가져와서 value로 삼으면 된다.암호화 된 텍스트의 숫자들을 reverse secret code를 이용하여 원래 글자들로 바꾼다. 문자열의 join method를 사용하여 글자 리스트를 하나의 문자열로 완성한다."

char_txt=set(test_txt) #set은 순서가 없는 집합이다. 실행할 때마다 순서가 다르다.
print(len(char_txt))


code_char= list(range(len(char_txt))) #숫자를 생성하고 리스트로 바꿔준다.
random.shuffle(code_char) #list를 막 shuffle해주고, 리스트 내용 자체를 변경
#방법 2: code_char=random.sample(code_char, len(code_char)) #만약 code_char에 저장하지 않으면, 변하지 않는다. 리스트 내용은 변경하지 않고, 결과만 리턴해준다. 반영하려면, 결과를 다시 저장해주어야 한다.

secret_code =dict(zip(char_txt, code_char))
print(secret_code)
print("-"*20,'원문을 암호화한 결과',"*"*20)
result_list=[]
for char in test_txt:
    result_list.append(secret_code[char]) #원문 텍스트의 글자 하나하나마다 매칭되는 암호 코드 찾아내기

print(result_list)
# 원상 복구 -> 암호화할 때 사용했던 secret code의 반대 사전이 필요함
decode_dict=dict(zip(secret_code.values(),secret_code.keys()))   #key: 암호코드 숫자, value : 원문 텍스트 숫자
print("-"*20,'원문을 복호화한 결과',"*"*20)
'''
resultD_list=[] #복호화한 결과를 저장할 변수
for code in result_list:
    resultD_list.append(decode_dict[code])
print(''.join(resultD_list)) #리스트 > 텍스트 : .join(리스트)
'''
resultD_list='' #복호화한 결과를 저장할 변수
for code in result_list:
    resultD_list+=decode_dict[code]
print(resultD_list) #리스트 > 텍스트 : 처음부터 스트링으로 받는다.
