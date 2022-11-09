"""내가 생각한 bobble sort
numbers = [5,4,1,3,9,2,15]
length= len(numbers)
for i in range(length):
    mini=numbers[i]
    for j in range(i+1,length):
        if mini>numbers[j]:
            mini=numbers[j]
            numbers[j]=numbers[i]
            numbers[i]=mini
print(numbers)
"""
#교수님이 알려주신 bubble sort=> 가까운 두개의 값을 비교해 바꾸어주는 것이다.
numbers =[5,4,1,3,9,2,15]

for i in range(0,len(numbers)):
    for j in range(0,len(numbers)-(i+1)):
        if numbers[j] > numbers[j+1]:
            tmp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=tmp
print(numbers)

