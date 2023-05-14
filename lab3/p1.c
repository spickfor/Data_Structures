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
	struct sll_node* tail_node;

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

		
		fprintf( stdout, "Data Value: %d\n", curr_ptr->data );
		// Iterate through the next node
		curr_ptr = curr_ptr->next_node;

	}
	fprintf( stdout, "\n" );

}

// function to to print Nth term in list
void displayNth(struct sllist *list) {
	int n;
	printf("Enter N: ");
	scanf("%d",&n);
	struct sll_node *current = list->head_node;
	for (int i = 1; i < n; i++) {
        current = current->next_node;
        if (current == NULL) {
            printf("Invalid N\n");
            return;
        }
    }

    printf("%d\n", current->data);
} 

// function to append to head or tail
void appendHeadOrTail(struct sllist *list) {
    char choice;
    printf("Enter H for head or T for tail: ");
    scanf(" %c", &choice);

    int value;
    struct sll_node *newNode = (struct sll_node *)malloc(sizeof(struct sll_node));
    if (choice == 'H') {
        printf("Enter a number less than %d: ", list->head_node->data);
        scanf("%d", &value);
        newNode->data = value;
        newNode->next_node = list->head_node;
        list->head_node = newNode;
    } else if (choice == 'T') {
        printf("Enter a number greater than %d: ", list->tail_node->data);
        scanf("%d", &value);
        newNode->data = value;
        newNode->next_node = NULL;
		list->tail_node = newNode;
	}
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

	// give options and get response
	int n;
	printf("1)Display all nodes\n2)Display nth node\n3)Append a new node - Head or Tail? (H/T)\n Choice:  ");
	scanf("%d",&n);

	switch (n)
	{
	case 1:
		// Step 11 - Call print in main
		printAll( the_list->head_node );
		break;
	case 2:
		displayNth(the_list);
		break;
	case 3:
		appendHeadOrTail(the_list);
		break;
	
	default:
		printf("Not a valid option");
		break;
	}
	



	// Step 9 - Call the destructor
	destructor( the_list->head_node );


	// Step 5 - Free the sllist
	free( the_list );

	return EXIT_SUCCESS;
}