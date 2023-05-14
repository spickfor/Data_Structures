/* Title: p2.c
 * Abstract: store integers in struct in ascending order using singly linked list
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 1.5hrs
 * Date: 2/7/23
*/


#include <stdio.h>
#include <stdlib.h>

// Define a struct called Node to store the value of the integer and a pointer to the next element in the list
struct Node {
  int data;
  struct Node *next;
};

// Define a struct named OrderedList to store integers in an ascending order
struct OrderedList {
  struct Node *head;
  struct Node *tail;
};

// Initialize the head and tail of the list
void initList(struct OrderedList *list) {
  list->head = NULL;
  list->tail = NULL;
}

// Create a new node with given value and insert it at the end of the list
void appendNode(struct OrderedList *list, int value) {
  struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = value;
  newNode->next = NULL;
  if (list->tail == NULL) {
    list->head = newNode;
    list->tail = newNode;
  } else {
    list->tail->next = newNode;
    list->tail = newNode;
  }
}

// Create a new node with given value and insert it at the beginning of the list
void insertNodeAtHead(struct OrderedList *list, int value) {
  struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = value;
  newNode->next = list->head;
  list->head = newNode;
}

// Display all nodes in the list (from head to tail)
void displayAll(struct OrderedList *list) {
  printf("Displaying all nodes:\n\t");
  struct Node *current = list->head;
  while (current != NULL) {
    if (current->next == NULL) {
      printf("%d ", current->data);
    }
    else {
      printf("%d -> ", current->data);
    }
    current = current->next;
  }
  printf("\n");
}

// Display the Nth node in the list
void displayNth(struct OrderedList *list, int n) {
  int i;
  struct Node *current = list->head;
  for (i = 1; i < n; i++) {
    current = current->next;
    if (current == NULL) {
      printf("Node %d not found.\n", n);
      return;
    }
  }
  printf("Displaying node %d:\n\t%d\n", n, current->data);
}

int main() {
  
char fileName[100];
  printf("Enter an input file: ");
  scanf("%s", fileName);
  FILE *file = fopen(fileName, "r");
  if (file == NULL) {
    printf("Error opening file.\n");
    return 0;
  }
  int n, i, value;
  fscanf(file, "%d", &n);
  struct OrderedList list;
  initList(&list);
  for (i = 0; i < n; i++) {
    fscanf(file, "%d", &value);
    appendNode(&list, value);
  }
  fclose(file);
  printf("Nodes entered into a singly linked list.\n");
  printf("This is a list of operations on the singly linked list: \n");
  printf("          1. Display all nodes\n");
  printf("          2. Display nth node\n");
  printf("          3. Append a new node - Head or Tail? (H/T)\n");
  
  char cont = 'y';
  char append;
  int nth_node;
  int n_append;

  while(cont == 'y') {
    printf("\nEnter your option: ");
    int choice;
    scanf("%d", &choice);

    switch (choice) {
      case 1:
        displayAll(&list);
	break;
      case 2:
        printf("Enter n to display nth node: ");
        scanf("%d", &nth_node);
        displayNth(&list, nth_node);
	break;
      case 3: 
        printf("Append to head or tail? (H/T): ");
	getc(stdin);
	scanf("%c", &append);
	if (append == 'T') {
	  printf("Node at the tail of the list is %d.\n", list.tail->data);
	  do {
	    printf("Enter an integer greater than %d to append to list: ", list.tail->data);
	    scanf("%d", &n_append);
	  } while (n_append <= list.tail->data);
	  appendNode(&list, n_append);
	}
	else if(append == 'H') {
	  printf("Node at the head of the list is %d.\n", list.head->data);
	  do {
	    printf("Enter an integer less than %d to append to list: ", list.head->data);
            scanf("%d", &n_append);
	  } while (n_append >= list.head->data);
	  insertNodeAtHead(&list, n_append);
	} 

	displayAll(&list); 
	break; 
	 
    }
    
    getc(stdin);
    printf("\nWould you like to continue? (y/n): ");
    scanf("%c", &cont);

  }
  
  return 0;
}
