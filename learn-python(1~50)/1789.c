#include <stdio.h>

int main() {
	long long a,b,c;
	scanf("%d",&b);
	while(1){a++;c+=a;if(c>b){a--;break;}}
	printf("%d\n",a);
}