'''
fq=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(len(fq)):
    for j in range(len(fq[0])):
        fq[i][j]=i+j
    print(i,"th row: ", fq[i])
print("*"*50)
print(fq)
'''
#2차원 리스트 성적처리
'''
s=[['kim',90,75],['park',89,95],['choi',76,85]]
average=0
for i in range(len(s)):
        print(s[i][0])
        sum=0
        for j in range(1,len(s[i])):
            sum+=s[i][j]
        average=sum/2.0
        print("sum = ",sum,"average = ",average)
'''
#구구단을 한 리스트 안에 정리 한다(2에서 16단까지)
numbers=[10*[0] for i in range(15)]
print (numbers)

for i in range(15):
    for j in range(10):
        numbers[i][j]=(i+2)*(j+1)
    print(numbers[i])
