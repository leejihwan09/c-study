#include <stdio.h>

int main() {
    int s;
    scanf("%d",&s);
    if (s<=100 && s>=90){
        printf("A");
    }
    else if (s<=89 && s>=80){
        printf("B");
    }
    else if (s<=79 && s>=70){
        printf("C");
    }
    else if (s<=69 && s>=60){
        printf("D");
    }
    else {
        printf("F");
    }
}