d=[]
for i in range(30):
    d.append(i+1)
for i in range(28):
    a=int(input())
    d.remove(a)
for i in d:
    print(i)