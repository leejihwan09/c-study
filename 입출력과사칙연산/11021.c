#include <stdio.h>

int main() {
  int i,t;
  scanf("%d", &t);
  for(i=1;i<=t;i++) {
    int a,b;
    scanf("%d%d",&a,&b);
    printf("Case #%d: %d\n",i,a+b);
  }

}