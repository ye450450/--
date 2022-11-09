print("예준 병원 온라인 예약 시스템")
date=0 #예약 날짜
name="" #환자 이름
symtom="" #증상
print('-'*20,'신규 예약','-'*20)
datelist=[] #예약날짜 리스트
namelist=[] #환자이름 리스트
symtomlist=[] #증상 리스트
while True:
    while True:
        date=input("예약날짜를 입력하시오.월2자리,일2자리 (0000) ")
        try:
            dateint=int(date)
            if len(date)==4:
                if date in datelist:
                    print("이미 예약이 되어있습니다. 다시 입력해주세요.")
                    continue
                datelist.append(date)
                break
            else:
                print("잘못입력했습니다.")
        except ValueError:
            print("잘못입력했습니다.")
    while True:
        name=input("환자이름을 입력하시오. ")
        if len(name) >=2:
            namelist.append(name)
            break
        else:
            print("잘못입력했습니다.")
    symtom=input("증상을 입력하시오. ")
    symtomlist.append(symtom)
    check=input("------------------예약을 추가로 하시겠습니까?(y를 입력하시오.) ")
    if check !='y':
        print("-"*20,"예약목록","-"*20)
        for i in range(len(datelist)):
            print("+"*3,"환자",i+1,"+"*3)
            print("예약날짜: ",datelist[i])
            print("환자이름: ",namelist[i])
            print("증상: ",symtomlist[i])
        break
        
        

    
