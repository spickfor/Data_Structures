/* Title: stretch.c
 * Abstract: uses only queue behaviors to decode a text file by reversing a string
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5hrs
 * Date: 2/15/23
*/


#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    char data;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct Queue {
    Node* front;
    Node* back;
} Queue;

void enque(Queue* q, char data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = q->back;

    if (q->back == NULL) {
        q->front = newNode;
    } else {
        q->back->next = newNode;
    }
    q->back = newNode;
}

char deque(Queue* q) {
    if (q->back == NULL) {
        return '\0';
    }

    char data = q->back->data;

    q->back = q->back->prev;

    if (q->back == NULL) {
        q->front = NULL;
    } else {
        q->back->next = NULL;
    }

    
    return data;
}

int isEmpty(Queue* q) {
    return (q->front == NULL);
}

int main() {
    Queue q1, q2;
    q1.front = NULL;
    q1.back = NULL;
    q2.front = NULL;
    q2.back = NULL;

    char filename[50];
    printf("file:  ");
    scanf("%s",&filename);
    FILE* fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    char c = fgetc(fp);
    while (c != EOF) {
        while (c != '\n' && c != EOF) {
            enque(&q1, c);
            c = fgetc(fp);
        }

        while (!isEmpty(&q1)) {
            printf("%c", deque(&q1));
        }

        while (!isEmpty(&q1)) {
            enque(&q2, deque(&q1));
        }

        while (!isEmpty(&q2)) {
            printf("%c", deque(&q2));
        }

        if (c == '\n') {
            printf("\n");
        }

        c = fgetc(fp);
    }

    fclose(fp);
    return 0;
}
