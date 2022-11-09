#같은 내용의 다른 측면을 담고 있는 여러개의 리스트가 있다고 하자.
# for 다음에 오는 것은 내가 만드는 임시 변수
list1 = ['mom','dad','me']
for e in list1:
    if e=='mom':
        print(e)
    
list2 = [50,52,20] #나이를 가진 list
myfamily = [['mom', 50],['dad',52],['me',20]] #비디오 7번에 나오는 내용이다.
#번호(index)를 이용하면 어래개의 리스트로부터 같은 대상을 동시에 추출
#이름과 나이를 동시에 출력하려면 어떻게 하면 좋을까?
print()
for i in range(len(list1)):
    print(list1[i] + ' ' + str(list2[i]))
    print(list2[i])
#range(len(list1)) -> 리스트의 길이만큼의 숫자를 리스트로 나타냄 즉, range(0,3)으로 출력됨

    
