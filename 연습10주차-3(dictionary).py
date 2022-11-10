'''
아이템이 없는 사전형 birthdate를 정의
사용자에게 이름과 생일을 입력 받아서 사전형 birthdate에 추가함
5명의 이름과 생일을 입력 받아서 추가한 후, 추가된 내용을 화면에 출력함
특정한 한 사람의 이름을 입력 받아서, 생일을 화면에 출력함
'''
birthdate={}
def add_birth(num):
    for i in range(num):
        name= input("이름을 입력하시오. ")
        birth= int(input("생일을 입력하시오. "))
        birthdate[name]={birth}
        print(name, birth)

add_birht(5)
search_name=input("검색할 이름을 입력하시오. ")
print(birthdate[search_name])

delete_name=input("삭제할 이름을 입력하시오. ")
birthdate.pop(delete_name)
print(delete_name in birthdate)
print(birhtdate)
