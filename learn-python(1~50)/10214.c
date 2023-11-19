#include <stdio.h>

int main() {
    int T,Y,K,O=0;
    scanf("%d",&T);
    for(int i=1;i<=T;i++) {
        for(int j=1;j<=9;j++) {
            scanf("%d%d",&Y,&K);
            O=O+Y-K;
        }
        if (O<0) {
            printf("Korea\n");
        }
        else if (O>0) {
            printf("Yonsei\n");
        }
        else {
            printf("Draw\n");
        }
    }
}