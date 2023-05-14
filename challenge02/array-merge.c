/* Title: array-merge.c
 * Abstract: This program merges two integer arrays into one ordered one
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5hrs
 * Date: 2/7/23
*/

#include <stdio.h>
#include <stdlib.h>

void merge(int *array1, int size1, int *array2, int size2, int *final) {
    //initilize variables for moving through
    int i = 0, j = 0, k = 0;
    // while loop to go through arrays
    while (i < size1 && j < size2) {
        // if statement compares values and then adds to final based on values
        if (array1[i] < array2[j]) {
            final[k++] = array1[i++];
        } else {
            final[k++] = array2[j++];
        }
    }
    
    while (i < size1) {
        final[k++] = array1[i++];
    }

    while (j < size2) {
        final[k++] = array2[j++];
    }
}

int main() {
    //initilize variables
    int n, m; 
    int i;
    char filename[20];
    // create pointers for arrays
    int *array1, *array2, *final;

    // prompt for file
    printf("Enter filename: ");
    scanf("%s", filename);

    // open file and check to make sure exists
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        printf("Could not open file.\n");
        return 1;
    }

    // scan file and read in numvalues of first
    fscanf(fp, "%d", &n);
    unsigned int mal_n = (unsigned int) n;
    // allocate mem for first array
    array1 = (int*)malloc(mal_n * sizeof(int));

    // read into first array
    for (i = 0; i < n; i++) {
        fscanf(fp, "%d", &array1[i]);
    }

    // scan file and read in numvalues for second array
    fscanf(fp, "%d", &m);
    unsigned int mal_m = (unsigned int) m;
    //allocate mem for second array
    array2 = (int*)malloc(mal_m * sizeof(unsigned int));

    // scan values into array 2
    for (i = 0; i < m; i++) {
        fscanf(fp, "%d", &array2[i]);
    }
    //close file
    fclose(fp);

    // allocate mem for final array
    final = (int*)malloc((mal_n + mal_m) * sizeof(unsigned int));
    // call the merge function
    merge(array1, n, array2, m, final);

    //print out values
    printf("Array1: ");
    for (i = 0; i < n; i++) {
        printf("%d ", array1[i]);
    }
    printf("\nArray1 size: %d\n", n);

    printf("Array2: ");
    for (i = 0; i < m; i++) {
        printf("%d ", array2[i]);
    }
    printf("\nArray2 size: %d\n", m);

    printf("Combined array: ");
    for (i = 0; i < n + m; i++) {
        printf("%d ", final[i]);
    }
    printf("\nCombined array size: %d\n", n + m);

    // free allocated mem
    free(array1);
    free(array2);
    free(final);

    return 0;
}
