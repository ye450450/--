import math

def formula(a,b,c):
    d=b**2-4*a*c
    if d>0:
        sol1=(-b+math.sqrt(d))/(2*a)
        sol2=(-b-math.sqrt(d))/(2*a)
        return sol1,sol2
    elif d==0:
        sol1= (-b/(2*a))
        return sol1
    else:
        return False

r= formula(1,5,4)
print(r)
