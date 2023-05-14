/* Title: struct-array.c
 * Abstract: This program determines average quiz scores of students within a course
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5 hrs
 * Date: 2/7/2023
*/

#include <stdio.h>
#include <stdlib.h>

#define QUIZ_COUNT 5

// create struct
typedef struct {
    char name[20];
    int id;
    float scores[QUIZ_COUNT];
    float average;
} Student;

// function that takes struct pointer and calculates avg
void calculate_average(Student *s) {
     float temp;
     int i, j;
     // for loop to parse all the quiz scores
     for (i = 0; i < 5; i++) {
        // for loop to parse 
        for (j = i + 1; j < 5; j++) {
            // organize scores with if
            if (s->scores[j] > s->scores[i]) {
                temp = s->scores[i];
                s->scores[i] = s->scores[j];
                s->scores[j] = temp;
            }
        }
    }
   float sum = 0;
    // take the average of the four highest scores
    for (i = 0; i < 4; i++) {
        sum += s->scores[i];
    }
    s->average = sum / 4;
}


int main() {
    int i, j, n;
    char filename[100];
    Student *students;

    // get filename
    printf("Enter an input file: ");
    scanf("%s", filename);

    // open file and make sure exist
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("File not found\n");
        exit(1);
    }

    // get number of students from first line of file
    fscanf(fp, "%d", &n);
    students = (Student *)malloc((unsigned int) n * sizeof(Student));

    //take vals from file and store in struct
    for (i = 0; i < n; i++) {
        fscanf(fp, "%s %d", students[i].name, &students[i].id);
        for (j = 0; j < QUIZ_COUNT; j++) {
            fscanf(fp, "%f", &students[i].scores[j]);
        }      
        // run user function
        calculate_average(&students[i]);
    }

    // output table and values
    printf("--------------------------------------------------\n");
    printf("  Course Report: Quiz Average\n");
    printf("--------------------------------------------------\n");
    for (i = 0; i < n; i++) {
        printf("  %-6s (%d):  %.3f\n", students[i].name, students[i].id, students[i].average);
    }
    printf("---------------------------------------------------\n");

    // close file and free mem
    fclose(fp);
    free(students);

    return 0;
}
