mystr="학문적 수월성과 인격적 덕성의 함양, 그리고 학문과 신앙의 유기적 통합은 한동대학교가 이 시대에 대하여 가지는 사명감입니다.또 우리는 모든 학생들이 21세기가 지도자로서 갖추어야 할 학문적 기초와 심도 있는 교양교육을 중요시합니다. 이를 잘 뒷받침하기 위해 한동기초학부가 있습니다."
#mystr안에 나타난 글자의 종류와 각 글자의 빈도수를 세어서 => 1. 반복문으로 하는 방법 // 2. set()을 이용하는 방법
#한줄에 하니씩 글자:빈도수 형식으로 출력하라
#이때 글자는 가나다라순으로 정렬하라
"""
spstr=list(mystr) #리스트로 변환
count =0
for i in spstr:
    for j in spstr:
        if(i ==j):
            count+=1
            print(i,":",count)
#교수님 답
uniqChar=[]
for ch in mystr:
    if not ch in uniqChar:
        uniqChar.append(ch)
print(uniqChar)

uniqChar.sort()

for uc in uniqChar:
    print(uc, ":", mystr.count(uc))
"""  
# uniqSet=set(mystr) #리스트와 같으나, 중복을 허용하지 않는 리스트
# noise가 많이 들어간 string -> tab, enter, space를 떼고 싶을 때, split과 join을 이용
print(' '.join("\t\t\t안녕하에요.....김예준입니다\n".split()))
tt= '안녕 {}야, 오늘 기온이 {:.2f}도 인데, 잘지내? '#소수점설정
tt= '안녕 {1}야, 오늘 기온이 {0}도 인데, 잘지내? '#순서설정
print(tt.format('지헌',17.4))
mydata =['지헌',17.4]
tt= '안녕 {0[0]}야, 오늘 기온이 {0[1]}도 인데, 잘지내? '#리스트를 받음
print(tt.format(mydata))

tt= '안녕 {name}야, 오늘 기온이 {temp}도 인데, 잘지내? '#리스트를 받음
print(tt.format(name='지헌',temp=17.4))

