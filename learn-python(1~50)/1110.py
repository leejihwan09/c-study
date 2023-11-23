a=int(input())
if a<10:
    f=[0,a]
else:
    f=list(str(a))
B=0
def cycle(x,y,B):
    if a==int(int(x)*10)+int(int(y)) and B>=1:
        return print(B)
    else:
        z=0
        z=int(x)+int(y)
        z=list(str(z))
        z.reverse()
        B+=1
        cycle(y,z[0],B)
cycle(f[0],f[1],B)