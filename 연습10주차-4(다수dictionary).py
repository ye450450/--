'''
친구 이름과 전화번홀 구성된 사전형 phone을 구성
아이템 추가로 5명의 자료를 입력, 이 때 입력은 함수로 구성
입력된 자료의 index만 모두 출력
입력된 자료의 값들만 모두 출력
'''
phone ={}

def add_phonenumber(n):
    for i in range(n):
        print(i+1)
        index=input('이름 : ')
        phonenumber = int(input("전화번호 : "))
        phone[index]=phonenumber

add_phonenumber(2)

print(phone.keys())
print(phone.values())
    
        

