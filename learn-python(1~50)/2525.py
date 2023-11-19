A,B = map(int,input().split())
C = int(input())
B+= C%60
C = C//60
if B>=60:
    B=B-60
    A=A+1
A+=C%24
if A>=24:
    A=A-24

print(f'{A} {B}')
