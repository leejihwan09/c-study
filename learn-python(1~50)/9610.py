list= [0]*5
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    if a>0 and b>0:
        list[0]+=1
    elif a>0 and b<0:
        list[3]+=1
    elif a<0 and b>0:
        list[1]+=1
    elif a<0 and b<0:
        list[2]+=1
    else:
        list[4]+=1
print(f'Q1: {list[0]}')
print(f'Q2: {list[1]}')
print(f'Q3: {list[2]}')
print(f'Q4: {list[3]}')
print(f'AXIS: {list[4]}')