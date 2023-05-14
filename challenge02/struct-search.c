/* Title: struct-search.c
 * Abstract: This program searches and finds customer info from bank data
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5 hrs
 * Date: 2/7/2023
*/

#include <stdio.h>
#include <string.h>
#define MAX_CUSTOMERS 30

//make struct
struct customer {
    char name[20];
    int account_number;
    float balance;
};

int main() {

    char filename[100];
    int num_customers, i, flag = 0;
    char search_name[20];
    //array of struct
    struct customer data[MAX_CUSTOMERS];

    // prompt for filename
    printf("Enter an input file: ");
    scanf("%s", filename);

    // open file and chekc if exist
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        printf("Unable to open file.\n");
        return 1;
    }
    
    // take in number of customers from first line
    fscanf(fp, "%d", &num_customers);

    // scan in the rest of file into struct
    for (i = 0; i < num_customers; i++) {
        fscanf(fp, "%s %d %f", data[i].name, &data[i].account_number, &data[i].balance);
    }

    // close file
    fclose(fp);

    char choice = 'y';
    // to create repetition with while loop
    while (choice == 'y') {
        flag = 0;
        printf("---------------------------------------------------\n");
        printf("  Record Finder - Enter a customer name: ");
        scanf("%s", search_name);
        printf("---------------------------------------------------\n");

        //parse to find customer if they exist
        for (i = 0; i < num_customers; i++) {
            if (strcmp(search_name, data[i].name) == 0) {
                printf("  Name: %s\n", data[i].name);
                printf("  Account: %d\n", data[i].account_number);
                printf("  Balance: %.2f\n", data[i].balance);
                flag = 1;
            }
        }
        // print they don't exist if not found
        if (!flag) {
            printf("  Fail. %s doesn't exist.\n", search_name);
        }
        printf("---------------------------------------------------\n");
        // prompt to continue loop
        printf("  Do you want to continue? (y/n) ");
        scanf(" %c", &choice);
    }
    // exit message
    printf("\n  Thank you for your service!\n");
    return 0;
}
