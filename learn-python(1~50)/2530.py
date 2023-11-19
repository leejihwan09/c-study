A,B,C = map(int,input().split())
D = int(input())
C += D % 60
D = D//60
if C>=60:
    C=C-60
    B=B+1
B += D % 60
D = D//60
if B>=60:
    B=B-60
    A=A+1
A += D % 24
if A>=24:
    A=A-24

print(f'{A} {B} {C}')