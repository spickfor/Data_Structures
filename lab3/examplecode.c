/* Title: p1.c
 * Abstract: store integers in struct in ascending order using singly linked list
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5hrs
 * Date: 2/7/23
*/


#include <stdio.h>
#include <stdlib.h>

// Step 1 - Create the struct for sll_node
typedef struct sll_node{
  
  // Step 2-1 - Create a int to hold data
	int data;

  // Step 2-2 - Create a struct to hold pointer to next node
	struct sll_node* next_node;

}sll_node;

// Step 3 - Create the struct for sllist
typedef struct sllist{

	// Make the sll_node member called head_node
	struct sll_node* head_node;

}sllist;


// Step 7 - Function to insert into singly linked list
void insert( sllist* the_list, int the_value ){

	// Create a sll_node pointer called insert_node
	sll_node* insert_node = (sll_node*)malloc( sizeof(sll_node) );

	// Set the insert_node's data to the_value and next_node to NULL
	insert_node->data = the_value;
	insert_node->next_node = NULL;

	// Check if the list is empty
	if( the_list->head_node == NULL ){

		// Set the head node equal to insert_node
		the_list->head_node = insert_node;

		// And return
		return;
	}

	// Otherwise, create a curr_ptr equal to the head_node
	sll_node* curr_ptr = the_list->head_node;

	// Iterate until the next_node is NULL
	while( curr_ptr->next_node != NULL ){

		curr_ptr = curr_ptr->next_node;
    
	}

	// Set curr_ptr's next_node equal to insert_node
	curr_ptr->next_node = insert_node;

}

// Step 10 - Print the Singly Linked List
void printAll( sll_node* head_node ){

	// Just change node_0 to head_node

	sll_node* curr_ptr = head_node;
	while( curr_ptr != NULL ){

		fprintf( stdout, "Node Base Address: %p\n", curr_ptr );
		fprintf( stdout, "Data Value: %d\n", curr_ptr->data );
		fprintf( stdout, "Location of Next Node: %p\n", &(curr_ptr->next_node) );
		fprintf( stdout, "Value of Next Node: %p\n\n", curr_ptr->next_node );

		// Iterate through the next node
		curr_ptr = curr_ptr->next_node;

	}
	fprintf( stdout, "\n" );

}


// Step 8 - Free all the elements
void destructor( sll_node* curr_ptr ){

	//Create a temporary pointer to hold the current pointer
  sll_node* tmp;
  
  // Check if curr_ptr is not NULL  
  while (curr_ptr != NULL) {  
    
    // Set temporary pointer to current pointer
    tmp = curr_ptr;

    //Set the current pointer to point to the next pointer in the list
    curr_ptr = curr_ptr->next_node;

    //Free the temporary pointer
    free(tmp);
  }
  return;

}


int main(){

	// Step 4 - Dynamically allocate a sllist
	sllist* the_list = (sllist *)malloc( sizeof( sllist ) );

	// Step 4-1 - Set the head_node to NULL
	the_list->head_node = NULL;

	fprintf( stdout, "Base Addresses: %p %p\n", &the_list, the_list );

	//Step 6 - Read values from file to insert into singly linked list
	FILE* ifptr = fopen("input.txt", "r");
	if (ifptr == NULL) {
		printf("File does not exist!");
		return 0;
	}

	int iter, the_value, num_values;
    //read first line that has number of values
	fscanf(ifptr,"%d", &num_values);
  
	// Call insert with as many as we want to insert
	for (iter = 0; iter < num_values; ++iter) {
		fscanf(ifptr,"%d", &the_value);
		insert( the_list, the_value );
	}

	
	// Step 11 - Call print in main
	fprintf( stdout, "\nHead Node Addresses: %p %p\n\n", &(the_list->head_node), the_list->head_node );
	printAll( the_list->head_node );


	// Step 9 - Call the destructor
	destructor( the_list->head_node );


	// Step 5 - Free the sllist
	free( the_list );

	return EXIT_SUCCESS;
}