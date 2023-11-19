#include <stdio.h>
#include <string.h> 

int main() {
    int T,R;
    char S[20];
    scanf("%d",&T);
    for(int i=1;i<=T;i++) {
    	scanf("%d%s",&R,S);
    	for(int y=0;y < strlen(S);y++) {
    		for(int l=0;l<R;l++) {
    			printf("%c",S[y]);
			}
		}
		printf("\n");
	}
}