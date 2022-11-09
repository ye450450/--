#맨 앞 글자가 b인 것만 삭제해라
f1=['apple','blueberry','melon','tomato']
f2=['strawberry','lemon','banana']
f3=f1+f2
for i in f3:
    if i[0]=='b':
        f3.remove(i)
print(f3)
