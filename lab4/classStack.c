#include <stdio.h>
#include <stdlib.h>

//Step 1 Create stack node struct
typedef struct stack_node{

  int data;

  struct stack_node *next;

}stack_node;

//Step 2 Create stack struct
typedef struct stack{

  struct stack_node *top;
	
}stack;


// Step 7 - Push into stack
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

// Step 11 - Print the Singly Linked List 
void print_stack( stack_node* curr_ptr ){

  printf ("Printing top to bottom...\n");
  while (curr_ptr != NULL) {
    printf("%d\n", curr_ptr->data);
    curr_ptr = curr_ptr->next;
  }
  	

}	


// Step 8 - Free all the elements 
void destructor( stack_node* curr_ptr ){

  // Create a tmp pointer
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


// Step 12 - Pop the top node
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


int main( const int argc, const char* argv[] ){

	//Step 3 - Dynamically allocate a stack 
	stack *the_stack = malloc (sizeof(stack));
	
	// Set the top to NULL 
  the_stack->top = NULL;

  //Step 5 - Read from a file and push into stack
  FILE *ifptr = fopen ("input.txt", "r");
  if(ifptr == NULL) {
    printf ("Couldn't open file ...\n");
  }

  int numValues, value;
  fscanf (ifptr, "%d", &numValues);
  //Step 6 - Call push on each value read from file
  for (int i = 0; i < numValues; i++) {
    fscanf(ifptr, "%d", &value);
    push(the_stack, value);
    // Step 10 - Call print stack
    print_stack(the_stack->top);
  }
	
	
	// Step 13 - Call pop until stack is empty
	 for (int i = 0; i < numValues; i++) {
    pop(the_stack);
    // Step 10 - Call print stack
    print_stack(the_stack->top);
  }

	
	// Step 9 - Call the destructor
	destructor(the_stack->top);

	
	// Step 4 - Free the stack 
  free (the_stack);
	
	
	return EXIT_SUCCESS;
}