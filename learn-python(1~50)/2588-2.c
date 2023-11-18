#include <stdio.h>
#include <stdlib.h>
int main() {
  int a;
  int b[3];
  int c;
  scanf("%d\n%1d%1d%1d", &a,&b[0],&b[1],&b[2]);
  c = b[0]*100 + b[1]*10 + b[2];
  printf("%d\n%d\n%d\n%d",b[2]*a,b[1]*a,b[0]*a,a*c);
  
}