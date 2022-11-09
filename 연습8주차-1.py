
def multiple(num1,num2):
    return num1*num2
a, b = input("두 개의 수를 입력하시오. ").split()
mul = multiple(int(a),int(b))
print(mul)

def exchange(listN,i,j):
    temp = listN[i]
    listN[i]=listN[j]
    listN[j]=temp

    
