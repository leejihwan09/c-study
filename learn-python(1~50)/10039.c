#include <stdio.h>

int main() {
	float a,b;
	int i;
    for(i=1;i<=5;i++){
        scanf("%f",&a);
        if(a<40)
        a=40;
        b+=a;
    }
	printf("%.f",b/5);
}