"""
while True:
    num = int(input("수를 입력하시오."))
    if num >=0:
        break
sumscore = 0 #평균 값을 계산하기위해
for i in range(num):
    score= int(input("점수를 입력하시오."))
    sumscore +=score
average= sumscore /float(num)
print("평균은 ",average)
"""
sung = ['김','최','이']
count =0
while True:
    name = input("이름을 입력하시오")
    if name[0] in sung:
        print(name[0],"씨가 존재합니다.")
        break
    count+=1
    if count>=5:
        print("5회 이상 입력하여 종료합니다.")
        break
