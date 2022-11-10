'''
함수를 실행하여 돌려 받은 값이 리스트일 때
돌려 받은 리스트를 튜플로 바꾼 후
문자열 "Kmoc"와 쌍을 구성하는 리스트로 바꾸기
'''
import random

def select_item(list,n):
    result= random.sample(list,n)
    return result
r=select_item([1,3,5,7,11,15,21],5)
print(r)
#여기까지가 주어진 코드
t=tuple(r)
pair=list(zip("Kmooc",t))
print(pair)
