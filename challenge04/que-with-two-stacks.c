/* Title: que-with-two-stacks.c
 * Abstract: Write a program to implement a queue using two stacks. Assume the only operations available to you are: push(), pop(), top() and isEmpty().
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 3 hrs
 * Date: 2/21/23
*/


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//stack node struct
typedef struct stack_node{
    int data;
    struct stack_node* next;
}stack_node;

//stack struct
typedef struct stack{
    struct stack_node* top;
}stack;


//Push into stack
void push(stack* the_stack, int val){
    //insert node
    stack_node* insert_node=malloc(sizeof(stack_node));
    insert_node->data=val;
    insert_node->next=NULL;
    //Check if the list is empty
    if(the_stack->top==NULL){
        the_stack->top=insert_node;
        return;
    }
    //Otherwise add insert_node to the top of the stack
    insert_node->next=the_stack->top;
    the_stack->top=insert_node;
}

//Free all the elements
void destructor(stack_node* curr_ptr){
    stack_node *tmp;
    while(curr_ptr!=NULL){
        tmp=curr_ptr;
        curr_ptr=curr_ptr->next;
        free(tmp);
    }
}

//Pop to top node
void pop(stack* the_stack){
    if(the_stack->top==NULL){
        return;
    }
    // Otherwise, move the top node to next and free old top node
    stack_node* tmp=the_stack->top;
    the_stack->top=the_stack->top->next;
    free(tmp);
}

int is_empty(stack* the_stack){
    if(the_stack->top==NULL){
        return 1;
    }
    return 0;
}

void top(stack* the_stack){
    if(the_stack->top==NULL) return;
    printf("%d", the_stack->top->data);
}

void enque(int val, stack* main_stack, stack* support_stack, int nodes){
    stack_node* main_node=main_stack->top;
    stack_node* support_node=support_stack->top;
    for(int i=1; i<=nodes; i++){
        push(support_stack, main_node->data);
        pop(main_stack);
        while(main_node->next!=NULL){
            main_node=main_node->next;
            support_node=support_node->next;
        }
    }
    push(main_stack, val);
    for(int i=1; i<=nodes; i++){
        push(main_stack, support_node->data);
        pop(support_stack);
    }
}

int deque(stack* main_stack){
    int pop_val=main_stack->top->data;
    pop(main_stack);
    return pop_val;
}

void display(stack_node* curr_ptr){
    printf(" Queue back to front..\n");
    while(curr_ptr!=NULL){
        printf("%d ", curr_ptr->data);
        curr_ptr=curr_ptr->next;
    }
}

int main(){
    char cont='Y';
    int option;
    int val=0;
    int nodes=0;

    stack* main_stack=malloc(sizeof(stack));
    main_stack->top=NULL;
    stack* support_stack=malloc(sizeof(stack));
    support_stack->top=NULL;


    printf("This is a list of operations to the que.\n\n");
    printf("\t1. Enque\n\t2. Deque\n\t3. Display\n");

    while(cont=='Y'){
        printf("\nEnter your option: ");
        scanf("%d", &option);
        switch(option){
            case 1:
            //enque
                printf("Enter value to enque: ");
                scanf("%d", &val);
                enque(val, main_stack, support_stack, nodes);
                break;
            case 2:
            //deque
                val=deque(main_stack);
                printf("Dequed element: %d\n", val);
                break;
            case 3:
            //display
                break;
            default:
                break;
            }
            display(main_stack->top);
            printf("\nContinue? (Y/N): ");
            scanf(" %c", &cont);
    }

    destructor(main_stack->top);
    free(main_stack);
    destructor(support_stack->top);
    free(support_stack);

    return 0;
}
