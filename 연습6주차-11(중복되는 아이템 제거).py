#두 개의 list를 생성, 중복되는 아이템을 제거, 두 개의 list를 합쳐 출력
list1=["사과","딸기","포도"]
list2=["청포도","딸기","풋사과"]
for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
            list2.remove(j)
list1.extend(list2)
print(list1)

'''교수님
for i in range(len(list1)):
    if list1[i] in list2:
        list2.remove(list1[i])
