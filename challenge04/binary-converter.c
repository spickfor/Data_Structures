/* Title: binary-converter.c
 * Abstract: uses the Stack code (from class) and prompts the user to enter a positive integer number, and uses a stack to convert that number to binary. 
   If the number is less than 1, exit the program. 
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5 hrs
 * Date: 2/20/23
*/


#include <stdio.h>
#include <stdlib.h>

// Create stack node struct
typedef struct stack_node{

  int data;

  struct stack_node *next;

}stack_node;

//Create stack struct
typedef struct stack{

  struct stack_node *top;
	
}stack;


// Push into stack
void push( stack* the_stack, int the_value ){

  // Create insert node
  stack_node *insert_node = malloc (sizeof(stack_node));
  insert_node->data = the_value;
  insert_node->next = NULL;
  
	// Check if the list is empty
  if (the_stack->top == NULL){
    the_stack->top = insert_node;
    //return
    return;
  }
    
	//Otherwise add insert_node to the top of the stack
  insert_node->next = the_stack->top;
  the_stack->top = insert_node;
	
}

// Print the Singly Linked List 
void print_stack( stack_node* curr_ptr,int value ){

    if(value < 1) return;

    printf ("%d => ",value);

    while (curr_ptr != NULL) {
      printf("%d", curr_ptr->data);
      curr_ptr = curr_ptr->next;
    }
}	


// Free all the elements 
void destructor( stack_node* curr_ptr ){

  // Create a tmp pointers
  stack_node *tmp;

  // Check if curr_ptr is NULL
  while(curr_ptr != NULL) {
    
    // Set tmp to point to curr_ptr
    tmp = curr_ptr;

    //Advance curr_ptr
    curr_ptr = curr_ptr->next;

    //free tmp
    free(tmp);
  }

}


// Pop the top node
void pop( stack* the_stack ){

 	// Check if the list is not empty
	if(the_stack->top == NULL) {
    return;
  }
	
	// Otherwise, move the top node to next and free old top node
  stack_node *tmp = the_stack->top;
  the_stack->top = the_stack->top->next;
  free(tmp); 
	
}


int main() {

	// Dynamically allocate a stack 
	stack *the_stack = malloc (sizeof(stack));
	
	// Set the top to NULL 
  the_stack->top = NULL;

  //Read from user
  int input;
  //while loop to repeat until 0 is input
  while(1) {
    printf("Enter a number: ");
    scanf("%d",&input);
    if(input < 1 && input != 0) {
      printf ("Number must be greater than 1\n");
      break;
    }
    else if (input == 0) {
      printf("Exiting\n");
      break;
    }
    
        // will hold the originally input number
        int temp = input;
    // use loop to convert to binary and push to stack
        int numValues = 0;
        while(input != 0) {
            if (input % 2 == 1) {
                push(the_stack,1);
            }
            else if (input % 2 == 0) {
                push(the_stack,0);
            }
            input = input/2;
            numValues++;
        }
        
        //print the stack
        print_stack(the_stack->top,temp);
        printf("\n");
    
        

        // Call pop until stack is empty
        for (int i = 0; i < numValues; i++) {
            pop(the_stack);
    }
  }
	
	// Call the destructor
	destructor(the_stack->top);

	
	// Free the stack 
  free (the_stack);
	
	
	return EXIT_SUCCESS;
}