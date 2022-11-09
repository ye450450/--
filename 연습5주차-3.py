"""
for i in range(10,0,-1):
    print(" "*i+"*"*(10-i)+"*"*(10-i))
"""
name = input("이름을 입력하시오")
count =0;
for i in name:
    if i!=" ":
        count+=1
    print(i)
print("총 글자 수는 = ",count)
