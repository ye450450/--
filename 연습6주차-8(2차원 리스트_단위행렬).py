number=int(input("수를 입력하시오. "))
listnum=[[0]*number for i in range(number)]
for i in range(number):
    for j in range(number):
        if i==j:
            listnum[i][j]=1
    print(listnum[i])
'''교수님
Size = int(input("행렬의 크기"))
temp_row=[]
Unit_Matrix =[]
for a in range(Size):
    for b in range(Size):
      temp_row.append(0)
    Unit_Matrix(temp_row)
    temp_row=[]
for i in range(Size):
    for j in range(Size):
      if i==j:
         Unit_Matrix[i][j]=1
    print(Unit_Matrix)
        
