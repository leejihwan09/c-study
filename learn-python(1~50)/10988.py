a = list(map(str,input()))
for i in range(int(len(a)/2)):
    if a[0]==a[-1]:
        del a[0]
        del a[-1]
if len(a)<=1:
    print(1)
else:
    print(0)
