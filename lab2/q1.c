// Seth Pickford
// q1.c

#include <stdio.h>
#include <stdlib.h>

struct data {
	char name[50];
	float num1;
	float num2;
	float avg;
} ;


int main() {

	struct data person[5];
	char filename[50];
	printf("Enter input file name:");
	scanf("%s",&filename);

	FILE *fp = fopen(filename,"r");
	if (fp == NULL) {
		printf("FILE DNE\n");
		return 1;
	}

	int i =0;
	while (!feof(fp)) {
		fscanf(fp,"%s %f %f",&person[i].name,&person[i].num1,&person[i].num2);
		i++;
	}


	fclose(fp);
	
	person[0].avg = (person[0].num1 + person[0].num2)/2;
	person[1].avg = (person[1].num1 + person[1].num2)/2;

	printf("%s avg: %.2f\n",person[0].name,person[0].avg);
	printf("%s avg: %.2f\n",person[1].name,person[1].avg);

	if (person[1].avg > person[0].avg) {
		printf("%s has greater average\n", person[1].name);
	}
	else printf("%s has greater average\n", person[2].name);

	return 0;	
}
