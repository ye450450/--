#유저가 'ㅋㅋㅋ'가 나올 때까지 유저로부터 좋아하는 과일을 입력받는다. / 과일 이름은 list/ 개수 출력
fruitli=[]
count=0
while True:
    fruit=input("좋아하는 과일은? ")
    if fruit == 'ㅋㅋㅋ':
        break
    fruitli.append(fruit)
    count+=1
print(fruitli, "개수 :",len(fruitli))
