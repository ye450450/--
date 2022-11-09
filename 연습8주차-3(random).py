import random

def input_list(li,num):
    for i in range(num):
        print(random.choice(li))
        
    #print(random.sample(li,num))와 같다.

name=["김","이","박","최","정"]
input_list(name,2)
 
def random_num(num1,num2):
    num=random.randrange(num1,num2)
    c=chr(65+num)
    print(num,c)

random_num(2,10)
