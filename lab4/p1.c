/* Title: p1.c
 * Abstract: uses only stack behaviors to decode a text file by reversing a strings
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5hrs
 * Date: 2/15/23
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char data;
    struct node *next;
} Node;

typedef struct stack {
    Node *head;
} Stack;

void push(Stack *stack, char data) {
    Node *new_node = (Node*) malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = stack->head;
    stack->head = new_node;
}

char pop(Stack *stack) {
    if (stack->head == NULL) {
        return '\0';
    }
    Node *temp = stack->head;
    char data = temp->data;
    stack->head = temp->next;
    free(temp);
    return data;
}

int is_empty(Stack *stack) {
    return stack->head == NULL;
}

char top(Stack *stack) {
    if (stack->head == NULL) {
        return '\0';
    }
    return stack->head->data;
}

void decode_line(char *line) {
    Stack stack;
    stack.head = NULL;
    int i = 0;
    while (line[i] != '\0') {
        push(&stack, line[i]);
        i++;
    }
    while (!is_empty(&stack)) {
        printf("%c", top(&stack));
        pop(&stack);
    }
    printf("\n");
}

int main() {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    char filename[50];
    printf("file: ");
    scanf("%s",&filename);
    fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: Could not open file\n");
        return 1;
    }
    while ((read = getline(&line, &len, fp)) != -1) {
        decode_line(line);
    }
    fclose(fp);
    if (line) {
        free(line);
    }
    return 0;
}
