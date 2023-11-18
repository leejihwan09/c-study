#include <stdio.h>

int main() {
	int i,t;
	int score_1=100,score_2=100;
	int dice1,dice2;
	scanf("%d",&t);
	for(i=1;i<=t;i++) {
		scanf("%d%d",&dice1,&dice2);
		if (dice1>dice2)
		score_2-= dice1;
		if (dice2>dice1)
		score_1-= dice2;	
	}
	printf("%d\n%d",score_1,score_2);
}