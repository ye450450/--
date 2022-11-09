#1111을 맞추거나 3회초과  틀리면 종료
password=''
count=0
while True:
    password=input('비밀번호를 입력하시오 ')
    if(password=='1111'):
        print('비밀번호가 맞습니다')
        break
    else:
        count+=1
        if count==3:
            print('3회 틀려 종료됩니다')
            break
        else:
            print(count, '회 시도했습니다. 다시 입력하시오 ')
