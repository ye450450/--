# 생년원일 8자리 받은 다음 앞의 4자리 생년을 slicing > 숫자로 형식을 바꿈 > 학번을 계산
# 조건문을 사용해서 1학년, 2학년, 3학년, 4학년, 입학 전, 졸업 출력
# 세대를 파악

birthday = input("생년원일 입력(8자리):")
year= int(birthday[0:4])
age= 2022-year+1
studentNum= 42-age
if(studentNum <19):
    print("졸업")
elif(studentNum ==19):
    print("4학년")
elif(studentNum ==20):
    print("3학년")
elif(studentNum ==21):
    print("2학년")
elif(studentNum ==22):
    print("1학년")
else:
    print("입학 전")
print("----------")

#세대 파악
#조건이 순차적으로 확장되는 경우 - 커트라인만 이용해서

if(year<1928):
    print("the greatest generation")
elif(year<1945):
    print("the silent generation")
elif(year<1964):
    print("baby boom generation")
elif(year<1980):
    print("generation x")
elif(year<1996):
    print("millennial generation 0r generation Y")
elif(year<2010):
    print("generation Z or iGen")
else:
    print("generation alpha")
