#include <stdio.h>
#include <stdlib.h>
int main() {
  int a;
  char b[3];
  scanf("%d\n%s", &a,b);
  printf("%d\n%d\n%d\n%d",a*(b[2]-'0'),a*(b[1]-'0'),a*(b[0]-'0'),a*atoi(b));

}