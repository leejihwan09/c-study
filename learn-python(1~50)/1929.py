import sys
a,b=map(int,sys.stdin.readline().split())
def prime_list(o,n):
    sieve=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    return [str(i) for i in range(o,n) if sieve[i] == True]
d=prime_list(a,b+1)
if '1'in d:d.remove('1')
print('\n'.join(d))