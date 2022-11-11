filename="poem.txt"
outf=open("numpoem.txt","w")
f= open(filename,"r")
sentence=[]
count=len(f.readlines())
f.close() #다시 읽기 위해 close를 해준다.

f=open(filename,"r")
for i in range(count):
    fline=f.readline()
    flist=fline.split()
    out.write(str(len(flist))+"\n")

f.close()
outf.close()
----------------------------------------------
#try except 구문을 사용하는 경우
'''
filename="poem.txt"
try:
    outf=open("numpoem.txt","w")
    f= open(filename,"r")
except IOError as err:
    print("unable to handle files")
sentence=[]
count=len(f.readlines())
f.close() #다시 읽기 위해 close를 해준다.

f=open(filename,"r")
for i in range(count):
    fline=f.readline()
    flist=fline.split()
    out.write(str(len(flist))+"\n")

f.close()
outf.close()
'''
