num = int(input("수를 입력하시오."))
check = False
for i in range(2,num):
    if num%i==0:
        print("소수가 아닙니다")
        check = True
        break
if check == False:
    print("소수입니다")
