#21900156 김예준 hw2
import random
import datetime

#임의의 날짜를 리턴하는 함수
def random_date():
    end = datetime.date.today() # 오늘 날짜를 저장
    start = datetime.date(2010,1,1) # 2010년 1월 1일을 저장
    return (start + datetime.timedelta(days=random.randint(0, int((end - start).days)))) #오늘과 2010년 1월 1일 사이의 임의 날짜를 반환해준다.

lname =[] #입력 받는 이름들을 받는 리스트 선언
lbirth =[] #저장한 이름에 부여된 생일들을 받는 리스트 선언
days = ['Mons. ','Tue .','Wed .','Thu .','Fri .','Sat .','Sun .'] #인덱스에 맞는 요일을 저장하는 리스트 
while(1): #3개 이상으이 이름이 입력되면 그만하도록 하기 위해 반복문을 선언
    name = input("Enter names seperated by comma: ") #이름들을 입력받고 저장
    vname= name.split(",") # ','로 구분한다.
    for i in vname: #입력받은 문자들을 하나씩 가져온다.
        if i.strip()!="": #공백들을 제거해주고, 만약 공백만 있지 않는 경우
            lname.append(i.strip()) #이름들을 저장하는 리스트에 추가해준다.
    lname= list(set(lname)) #반복되는 것들을 없애준다.
    print("Valid names received are",lname) #유효한 이름들을 출력해준다.
    if len(lname)>=3: #만약 3가지 이상 입력을 받으면 더이상 입력받지 않아도 되어 반복문을 빠져나간다.
        break
    else:
        print("The number of valid names is less than 3.") #유효한 이름이 3개보다 적으면 적다고 말해주고 다시 반복한다. 
for i in range(0,len(lname)): #유효한 이름 개수만큼 반복해준다.
    lbirth.append(random_date()) #임의의 날짜들을 생일을 받는 리스트에 넣어준다.
print("*"*20) #구분선을 출력한다.
for i in range(0,len(lname)): #유효한 이름 개수만큼 반복해준다.
    print(lname[i],lbirth[i]) #유료한 이름과 그에 부여된 생일들을 출력한다.
print("*"*20) #구분선을 출력한다.
while(1): #'y' 외의 문자를 입력받으면 반복을 그만하도록 하기 위해 반복문을 선언한다.
    while(1): #유효한 이름과 같은 이름을 입력받을 떄까지 입력받기 위해 반복문을 선언한다.
        chosename=input("Please choose your character among "+str(lname)+": " ) #유효한 이름 목록 중에 한 명을 입력하라고 하고 이를 변수에 저장한다.
        if(chosename in lname): #만약 유효한 이름 리스트에 입력받은 값이 존재한다면
            chosebirth = lbirth[lname.index(chosename)] #입력받은 이름에 맞는 인덱스 위치에 있는 생일날짜를 변수에 저장한다. 
            day= chosebirth.weekday() #생일날짜에 맞는 요일(정수값)을 변수에 저장한다. 
            print("You have chosen "+chosename+" born in "+str(chosebirth)+" ("+days[day]+")") #사용자가 고른 이름과 생일과 요일을 출력해준다.
            break #반복문을 빠져나간다. 
    comchose= random.choice(lname) #이름 리스트 중에서 랜덤으로 골라 변수에 저장한다. 
    combirth= lbirth[lname.index(comchose)] #이름에 알맞는 생일을 변수에 저장한다.
    comday= combirth.weekday() #고른 생일에 맞는 요일(정수값)을 변수에 저장한다.
    print("The computer has chosen "+comchose+ " born in "+str(combirth)+" ("+days[comday]+")") #컴퓨터가 고른 이름과 생일과 요일을 출력해준다.
    if(chosename==comchose): #만약 사용자가 고른 이름과 컴퓨터가 고른 이름과 같은 경우
        print("They are the same person") #같은 사람이라고 출력해준다.
    else: #사용자가 고른 이름과 컴퓨터가 고른 이름과 같지 않은 경우
        if combirth > chosebirth : #컴퓨터가 고른 이름의 생일이 사용자가 고른 이름의 생일보다 큰 경우(날짜자체)
            print(chosename+" is older than "+comchose) #사용자가 고른 이름이 컴퓨터가 고른 이름보다 나이가 많다고 출력한다.
        elif combirth < chosebirth: #사용자가 고른 이름의 생일이 컴퓨터가 고른 이름의 생일보다 큰 경우(날짜자체)
            print(comchose+" is older than "+chosename) #컴퓨터가 고른 이름이 사용자가 고른 이름보다 나이가 많다고 출력한다.
        else: #사용자가 고른 이름의 생일이 컴퓨터가 고른 이름의 생일과 같은 경우(날짜자체)
            print("They are same age") #나이가 같다고 출력해준다.
    check=input("Do you want to play again? (y): ") #다시 하겠냐고 물어보고 이를 변수에 저장한다.
    if check!="y": #만약 'y'외의 문자를 입력받으면
        break #반복문을 나가 프로그램을 종료한다.
