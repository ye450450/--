kor=float(input("국어과목 점수?"))
math=float(input("수학과목 점수?"))
eng=float(input("영어과목 점수?"))
average=(kor+math+eng)/3
print(average)
if average <60 or (math<50 or kor<50 or eng<50):
        print("불합격입니다")
else:
    print("합격입니다.")
