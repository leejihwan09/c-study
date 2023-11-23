for i in reversed(range(int(input()))):
    for j in range(i+1):
        print('*',end='')
    if j!=i+1:
        print()