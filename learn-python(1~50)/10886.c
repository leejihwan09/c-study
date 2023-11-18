#include <stdio.h>

int main() {
	int n,a=0,i;
	float b;
	scanf("%d",&n);
	for(i=1;i<=n;i++) {
		scanf("%d",&a);
		
    	if(a==1){
    		b++;
		}
	}
	if(b/n> 0.5)
	printf("Junhee is cute!");
	if(b/n< 0.5)
	printf("Junhee is not cute!");
}