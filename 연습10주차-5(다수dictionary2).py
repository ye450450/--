'''
교사명과 담당교과목명을 사전형으로 구성함
- '김경미''수학','과학'
- '최영희''영어','수학'
- '강동원''영어'
- '정필수''사회','역사'
- '박희수''국어'
- '이승철''수학','과학'
- 담당교과목명을 입력하면 교사명을 출력함
- 담당교과목을 여러명의 교사가 강의하는 경우, 모든 교사명을 다 출력함.
'''
def find_teacher(sub):
    Subjects={'김경미':['수학','과학'],'최영희':['영어','수학'],'강동원':'영어',
              '정필수':['사회','역사'],'박희수':'국어','이승철':['수학','과학']}

    teacher=[]
    for key in Subjects.keys():
        if sub in Subjects[key]:
            teacher.append(key)
    return teacher

sub=input("과목을 입력하시오: ")
print(find_teacher(sub))
