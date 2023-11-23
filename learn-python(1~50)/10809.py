b=input()
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in b:
        print(b.index(i),end=' ')
    else:
        print(-1,end=' ')
