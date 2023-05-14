// Seth Pickford
//q2.c

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int *append(int *array,int size,int input);
int *delete(int *array,int size, int input);

int main() {

    bool cont = true;
    // filename
    char filename[50] = "input_array_resize.txt";

    // open file and create pointer to it
	FILE *fp = fopen(filename,"r");
	if (fp == NULL) {
		printf("FILE DNE\n");
		return 1;
	}

    // get size of array
    int arraysize;
    fscanf(fp,"%d",&arraysize);
    
    // allocate mem for array
    int* array;
    array = malloc(arraysize * sizeof(int));

    //checking to make sure mem can be allocated
    if (array == NULL) {
        printf("Unable to allocate memory\n");
        return 1;
    }

    // read in the array
	for (int i =0; i < arraysize;i++) {
		fscanf(fp, "%d", &array[i]);
	}

    //close file
    fclose(fp);

    printf("given array: ");
    for (int i=0;i< arraysize;i++) {
        printf("%d  ",array[i]);
    }

    printf("\n");

    // while loop to repeat
    while(cont) {

    // propmt user for action type
    printf("1:append num\n2:delete num\n Input:");
    int input;
    scanf("%d",&input);


     

    // switch statement to control action
    switch(input) {
        case 1:
            printf("Number to append: ");
            scanf("%d",&input); 
            
            array = append(array,arraysize,input);   
            arraysize++;
            break;
        case 2:
            printf("Number to delete: ");
            scanf("%d",&input);
            array = delete(array,arraysize,input);
            arraysize--;
            break;
        default:
            printf("not an option\n");
            return 1;
    }
    printf("\n");
    printf("array size: %d",arraysize);

        printf("\n");
        printf("Continue(y or n) : ");
        char userinput;
        getc(stdin);
        scanf("%c",&userinput);

        // control if repeats
        if(userinput=='y') cont = true;
        else if(userinput =='n') cont = false;
        else {
            printf("wrong input\n");
            return 1;
        }

    }

    free(array);

    printf("\n");
    return 0;
}

int *append(int *array,int size,int input) {


    // allocatte mem for new array
    int* array2;
    array2 = malloc((size+1) * sizeof(int));


    // set arrays equal
    for (int i=0;i< size;i++) {
            array2[i] = array[i];
}
    //add appended number
    array2[size] = input;

    //print the new array
    printf("new array:  ");
    for (int i=0;i< size+1;i++) {
        printf("%d  ",array2[i]);
    }

    free(array);
    return array2;

}




int *delete(int *array,int size,int input) {
    
    // allocatte mem for new array
    int* array2;
    array2 = malloc((size) * sizeof(int));

    //checking to make sure mem can be allocated
    if (array2 == NULL) {
        printf("Unable to allocate memory\n");
         return array;
    }

    // set arrays equal and remove number
        int j =0;
    for (int i=0;i< size;i++) {
        if(input!=array[i]) {
            array2[j] = array[i];
            j++;
        }
        
}

    //print the new array
    printf("new array:  ");
    for (int i=0;i< size-1;i++) {
        printf("%d  ",array2[i]);
    }
    free(array);


    return array2;

}