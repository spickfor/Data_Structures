/* Title: dll-ordered-list-stretch.c
 * Abstract: defines a struct named OrderedList to store integers in an ascending order.  USes a doubly linked list to do this
 * Author: Seth Pickford
 * Email: spickfor@nd.edu
 * Estimate: 2 hrs
 * Date: 2/16/23
*/


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

                                                                                                                                                                                                               
// create structs for doubly linked
typedef struct Node {                                                                                                                                                                                         
    int data;                                                                                                                                                                                                 
    struct Node* next;                                                                                                                                                                                         
    struct Node* prev;                                                                                                                                                                                         
} Node;                                                                                                                                                                                                                                                                                                                                                                                                                     

typedef struct OrderedList {                                                                                                                                                                                  
    Node* head;                                                                                                                                                                                                
    Node* tail;                                                                                                                                                                                                
    int count;                                                                                                                                                                                                 
} OrderedList;                                                                                                                                                                                                 

                                                                                                                                                                                                               
// displays all of the nodes
void displayAll(OrderedList* list) {                                                                                                                                                                          
    Node* curr = list->head;                                                                                                                                                                                   
    while (curr != NULL) {                                                                                                                                                                                     
        printf("%d ", curr->data);                                                                                                                                                                             
        curr = curr->next;                                                                                                                                                                                    
    }                                                                                                                                                                                                          
    printf("\n");                                                                                                                                                                                              
}                                                                                                                                                                                                                                                                                                                                                                                                                        

//display the node at a specified spot in the list of nodes
void displayNth(OrderedList* list) {                                                                                                                                                                           
    int n;                                                                                                                                                                                                    
    printf("Enter the index of the node to display: ");                                                                                                                                                       
    scanf("%d", &n);                                                                                                                                                                                                                                                                                                                                                                                                 

    Node* curr = list->head;                                                                                                                                                                                   
    int i = 0;                                                                                                                                                                                                
    while (curr != NULL && i < n) {                                                                                                                                                                           
        curr = curr->next;                                                                                                                                                                                     
        i++;                                                                                                                                                                                                   
    }                                                                                                                                                                                                                                                                                                                                                                                                                    

    if (curr == NULL) {                                                                                                                                                                                       
        printf("Error: index out of bounds\n");                                                                                                                                                                
    }
    else {                                                                                                                                                                                                   
        printf("Node %d: %d\n", n, curr->data);                                                                                                                                                                
    }                                                                                                                                                                                                          
}                                                                                                                                                                                                             
                                                                                                                                                                                                            
//adds a new node either to the head or tail, dependent upon input
void appendHeadOrTail(OrderedList* list,int reverse) {                                                                                                                                                                     
    char choice;                                                                                                                                                                                               
    printf("Do you want to append the new node to head (H) or tail (T)? ");                                                                                                                                    
    scanf(" %c", &choice);                                                                                                                                                                                                                                                                                                                                                                                             

    if(reverse > 0) {
        int newData;                                                                                                                                                                                               
        if (choice == 'H') {
            do {                                                                                                                                                                                       
            printf("Enter the new value (less than the current head %d): ", list->head->data);                                                                                                                     
            scanf("%d", &newData);                                                                                                                                                                                                                                                                                                                                                                                       
            } while (newData >= list->head->data);
            Node* newNode = (Node*)malloc(sizeof(Node));                                                                                                                                                           
            newNode->data = newData;                                                                                                                                                                               
            newNode->prev = NULL;                                                                                                                                                                                  
            newNode->next = list->head;                                                                                                                                                                                                                                                                                                                                                                                     

           list->head->prev = newNode;                                                                                                                                                                           
           list->head = newNode;                                                                                                                                                                                  

        } 
        else if (choice == 'T') {
            do {                                                                                                                                                                                
            printf("Enter the new value (greater than the current tail %d): ", list->tail->data);                                                                                                                  
            scanf("%d", &newData);                                                                                                                                                                                
            } while(newData <= list->tail->data);                                                                                                                                                                                                  
            Node* newNode = (Node*)malloc(sizeof(Node));                                                                                                                                                          
            newNode->data = newData;                                                                                                                                                                               
           newNode->prev = list->tail;                                                                                                                                                                            
           newNode->next = NULL;                                                                                                                                                                                  
                                                                                                                                                                                                               
           list->tail->next = newNode;                                                                                                                                                                           
           list->tail = newNode;                                                                                                                                                                                  
       } 
       else {                                                                                                                                                                                                   
           printf("Error: invalid choice\n");                                                                                                                                                                     
           return;                                                                                                                                                                                               
        }
    }
    else if (reverse < 0) {
        int newData;                                                                                                                                                                                               
        if (choice == 'H') {                                                                                                                                                                                       
            printf("Enter the new value (greater than the current head %d): ", list->head->data);                                                                                                                     
            scanf("%d", &newData);                                                                                                                                                                                                                                                                                                                                                                                       

            Node* newNode = (Node*)malloc(sizeof(Node));                                                                                                                                                           
            newNode->data = newData;                                                                                                                                                                               
            newNode->prev = NULL;                                                                                                                                                                                  
            newNode->next = list->head;                                                                                                                                                                                                                                                                                                                                                                                     

           list->head->prev = newNode;                                                                                                                                                                           
           list->head = newNode;                                                                                                                                                                                  

        } 
        else if (choice == 'T') {                                                                                                                                                                                
            printf("Enter the new value (less than the current tail %d): ", list->tail->data);                                                                                                                  
            scanf("%d", &newData);                                                                                                                                                                                
                                                                                                                                                                                                               
            Node* newNode = (Node*)malloc(sizeof(Node));                                                                                                                                                          
            newNode->data = newData;                                                                                                                                                                               
           newNode->prev = list->tail;                                                                                                                                                                            
           newNode->next = NULL;                                                                                                                                                                                  
                                                                                                                                                                                                               
           list->tail->next = newNode;                                                                                                                                                                           
           list->tail = newNode;                                                                                                                                                                                  
       } 
       else {                                                                                                                                                                                                   
           printf("Error: invalid choice\n");                                                                                                                                                                     
           return;                                                                                                                                                                                               
        }
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    displayAll(list);                                                                                                                                                                                          
}                                                                                                                                                                                                              
                                                                                                                                                                                                               
//adds node to nth position in list
void appendNthPosition(OrderedList* list) {                                                                                                                                                                   
    int n;                                                                                                                                                                                                     
    printf("Enter the index of the new node: ");                                                                                                                                                               
    scanf("%d", &n);                                                                                                                                                                                           
                                                                                                                                                                                                               
    int inverse = 1;
    if (n == 0) {                                                                                                                                                                                             
        appendHeadOrTail(list,inverse);                                                                                                                                                                                
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    Node* prevNode = list->head;                                                                                                                                                                              
    int i = 0;                                                                                                                                                                                                 
    while (prevNode != NULL && i < n-1) {                                                                                                                                                                      
        prevNode = prevNode->next;                                                                                                                                                                             
        i++;                                                                                                                                                                                                   
    }                                                                                                                                                                                                         
                                                                                                                                                                                                               
    if (prevNode == NULL) {                                                                                                                                                                                    
        printf("Error: index out of bounds\n");                                                                                                                                                                
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    Node* nextNode = prevNode->next;                                                                                                                                                                          
    if (nextNode == NULL) {                                                                                                                                                                                    
        appendHeadOrTail(list,inverse);                                                                                                                                                                                
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                         
                                                                                                                                                                                                               
    int newData;
    do {                                                                                                                                                                                               
    printf("Enter the new value (between %d and %d): ", prevNode->data, nextNode->data);                                                                                                                       
    scanf("%d", &newData);                                                                                                                                                                                     
    } while(newData <= prevNode->data || newData >= nextNode->data);                                                                                                                                                                                                         
    Node* newNode = (Node*)malloc(sizeof(Node));                                                                                                                                                              
    newNode->data = newData;                                                                                                                                                                                   
    newNode->prev = prevNode;                                                                                                                                                                                  
    newNode->next = nextNode;                                                                                                                                                                                                                                                                                                                                                                                                
    prevNode->next = newNode;                                                                                                                                                                                 
    nextNode->prev = newNode;                                                                                                                                                                                  
                                                                                                                                                                                                               
    displayAll(list);                                                                                                                                                                                          
}                                                                                                                                                                                                              
                                                                                                                                                                                                               
// Delete the head or tail node based on user input                                                                                                                                                        
void deleteHeadOrTail(OrderedList *list) {                                                                                                                                                                     
    char choice;                                                                                                                                                                                               
    Node *temp;                                                                                                                                                                                                
    if (list->head == NULL) {                                                                                                                                                                                 
        printf("The list is empty.\n");                                                                                                                                                                       
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
    printf("Do you want to delete head or tail? (H/T): ");                                                                                                                                                     
    scanf(" %c", &choice);                                                                                                                                                                                     
    if (toupper(choice) == 'H') {                                                                                                                                                                             
        temp = list->head;                                                                                                                                                                                     
        list->head = list->head->next;                                                                                                                                                                         
        if (list->head != NULL) {                                                                                                                                                                              
            list->head->prev = NULL;                                                                                                                                                                           
        } 
        else {                                                                                                                                                                                              
            list->tail = NULL;                                                                                                                                                                                
        }                                                                                                                                                                                                      
    } 
    else if (toupper(choice) == 'T') {                                                                                                                                                                       
        temp = list->tail;                                                                                                                                                                                     
        list->tail = list->tail->prev;                                                                                                                                                                        
        if (list->tail != NULL) {                                                                                                                                                                             
            list->tail->next = NULL;                                                                                                                                                                          
        } 
        else {                                                                                                                                                                                               
            list->head = NULL;                                                                                                                                                                                 
        }                                                                                                                                                                                                      
    } 
    else {                                                                                                                                                                                                  
        printf("Invalid input.\n");                                                                                                                                                                           
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
    printf("Deleted node: %d\n", temp->data);                                                                                                                                                                  
    free(temp);                                                                                                                                                                                                
}                                                                                                                                                                                                             
                                                                                                                                                                                                               
// Delete the Nth node in the list                                                                                                                                                                          
void deleteNthNode(OrderedList *list) {                                                                                                                                                                        
    int n, i;                                                                                                                                                                                                  
    Node *temp;                                                                                                                                                                                               
    if (list->head == NULL) {                                                                                                                                                                                 
        printf("The list is empty.\n");                                                                                                                                                                        
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
    printf("Enter the position of the node you want to delete: ");                                                                                                                                           
    scanf("%d", &n);                                                                                                                                                                                          
    temp = list->head;                                                                                                                                                                                         
    if (n == 1) {                                                                                                                                                                                              
        list->head = list->head->next;                                                                                                                                                                         
        if (list->head != NULL) {                                                                                                                                                                              
            list->head->prev = NULL;                                                                                                                                                                          
        } 
        else {                                                                                                                                                                                               
            list->tail = NULL;                                                                                                                                                                                 
        }                                                                                                                                                                                                      
        printf("Deleted node: %d\n", temp->data);                                                                                                                                                              
        free(temp);                                                                                                                                                                                           
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
    for (i = 1; i < n && temp != NULL; i++) {                                                                                                                                                                  
        temp = temp->next;                                                                                                                                                                                     
    }                                                                                                                                                                                                         
    if (temp == NULL) {                                                                                                                                                                                       
        printf("Node not found.\n");                                                                                                                                                                           
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
    temp->prev->next = temp->next;                                                                                                                                                                             
    if (temp->next != NULL) {                                                                                                                                                                                 
        temp->next->prev = temp->prev;                                                                                                                                                                        
    } 
    else {                                                                                                                                                                                                   
        list->tail = temp->prev;                                                                                                                                                                               
    }                                                                                                                                                                                                          
    printf("Deleted node: %d\n", temp->data);                                                                                                                                                                 
    free(temp);                                                                                                                                                                                                
}                                                                                                                                                                                                             
                                                                                                                                                                                                        
// Find the user entered integer in the list                                                                                                                                                                
void find(OrderedList *list) {                                                                                                                                                                                
    int searchValue;                                                                                                                                                                                          
    printf("Enter the value to search: ");                                                                                                                                                                     
    scanf("%d", &searchValue);                                                                                                                                                                                 
                                                                                                                                                                                                               
    Node *currentNode = list->head;                                                                                                                                                                           
    int currentPosition = 1;                                                                                                                                                                                  
    while (currentNode != NULL) {                                                                                                                                                                             
        if (currentNode->data == searchValue) {                                                                                                                                                                
            printf("Found %d at position %d\n", searchValue, currentPosition);                                                                                                                                 
            return;                                                                                                                                                                                            
        }                                                                                                                                                                                                      
        currentNode = currentNode->next;                                                                                                                                                                      
        currentPosition++;                                                                                                                                                                                     
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    printf("%d not found in the list\n", searchValue);                                                                                                                                                         
}                                                                                                                                                                                                             
                                                                                                                                                                                                               
// Count the number of nodes in the list                                                                                                                                                                    
void getNumberOfNodes(OrderedList *list) {                                                                                                                                                                     
    int count = 0;                                                                                                                                                                                             
    Node *temp = list->head;                                                                                                                                                                                  
    while (temp != NULL) {                                                                                                                                                                                    
        count++;                                                                                                                                                                                               
        temp = temp->next;                                                                                                                                                                                     
    }                                                                                                                                                                                                          
    printf("The number of nodes in the list is %d.\n", count);                                                                                                                                                 
}                                                                                                                                                                                                             
                                                                                                                                                                                                               
//display all even numbers in list
void displayEven(OrderedList *list) {                                                                                                                                                                          
    if (list == NULL || list->head == NULL) {                                                                                                                                                                  
        printf("List is empty!\n");                                                                                                                                                                            
        return;                                                                                                                                                                                               
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    Node *curr = list->head;                                                                                                                                                                                   
    int index = 1;                                                                                                                                                                                             
                                                                                                                                                                                                               
    printf("Even Nodes: ");                                                                                                                                                                                   
    while (curr != NULL) {                                                                                                                                                                                     
        if (curr->data % 2 == 0) {                                                                                                                                                                             
            printf("%d ", curr->data);                                                                                                                                                                         
        }                                                                                                                                                                                                      
        curr = curr->next;                                                                                                                                                                                    
        index++;                                                                                                                                                                                               
    }                                                                                                                                                                                                          
    printf("\n");                                                                                                                                                                                              
}                                                                                                                                                                                                              

//display odd numbers in list                                                                                                                                                                                                            
void displayOdd(OrderedList *list) {                                                                                                                                                                          
    if (list == NULL || list->head == NULL) {                                                                                                                                                                  
        printf("List is empty!\n");                                                                                                                                                                            
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                         
Node *curr = list->head;                                                                                                                                                                                   
    int index = 1;                                                                                                                                                                                             
                                                                                                                                                                                                               
    printf("Odd Nodes: ");                                                                                                                                                                                     
    while (curr != NULL) {                                                                                                                                                                                    
        if (curr->data % 2 == 1) {                                                                                                                                                                           
            printf("%d ", curr->data);                                                                                                                                                                        
        }                                                                                                                                                                                                      
        curr = curr->next;                                                                                                                                                                                     
        index++;                                                                                                                                                                                              
    }                                                                                                                                                                                                          
    printf("\n");                                                                                                                                                                                              
}                                                                                                                                                                                                             
                                                                                                                                                                                                               
//reverse order of list
void reverseList(OrderedList *list) {                                                                                                                                                                         
    if (list == NULL || list->head == NULL) {                                                                                                                                                                 
        printf("List is empty!\n");                                                                                                                                                                           
        return;                                                                                                                                                                                                
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    Node *temp = NULL;                                                                                                                                                                                         
    Node *curr = list->head;                                                                                                                                                                                  
                                                                                                                                                                                                               
    while (curr != NULL) {                                                                                                                                                                                     
        temp = curr->prev;                                                                                                                                                                                     
        curr->prev = curr->next;                                                                                                                                                                               
        curr->next = temp;                                                                                                                                                                                    
        curr = curr->prev;                                                                                                                                                                                    
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    temp = list->head;                                                                                                                                                                                         
    list->head = list->tail;                                                                                                                                                                                  
    list->tail = temp;                                                                                                                                                                                        
}                                                                                                                                                                                                              
                                                                                                                                                                                                               
//used for clearing up used memory space
void destroyList(OrderedList *list) {                                                                                                                                                                          
    Node *current = list->head;                                                                                                                                                                                
    Node *next;                                                                                                                                                                                               
                                                                                                                                                                                                            
    while (current != NULL) {                                                                                                                                                                                  
        next = current->next;                                                                                                                                                                                  
        free(current);                                                                                                                                                                                         
        current = next;                                                                                                                                                                                       
    }                                                                                                                                                                                                          
                                                                                                                                                                                                               
    list->head = NULL;                                                                                                                                                                                         
    list->tail = NULL;                                                                                                                                                                                         
    list->count = 0;                                                                                                                                                                                          
}                                                                                                                                                                                                              
                                                                                                                                                                                                               
int main() {                                                                                                                                                                                                   
    OrderedList list = {NULL, NULL, 0};                                                                                                                                                                        
    
    //take filename and open fill
    FILE *fp;                                                                                                                                                                                                  
    char filename[50];                                                                                                                                                                                        
    printf("Enter filename: ");                                                                                                                                                                                
    scanf("%s", filename);                                                                                                                                                                                     
    fp = fopen(filename, "r");  

    //if file doesn't exist print error
    if (fp == NULL) {                                                                                                                                                                                          
        printf("Error opening file\n");                                                                                                                                                                       
        return 1;                                                                                                                                                                                              
    }                                                                                                                                                                                                          

    int n;                                                                                                                                                                                                     
    //take number of nodes
    fscanf(fp, "%d", &n);                                                                                                                                                                                      

    //scan in values from file
    int i;                                                                                                                                                                                                    
    for (i = 0; i < n; i++) {                                                                                                                                                                                 
        int val;                                                                                                                                                                                               
        fscanf(fp, "%d", &val);                                                                                                                                                                                

        if (i == 0) {                                                                                                                                                                                          
            list.head = (Node *)malloc(sizeof(Node));                                                                                                                                                          
            list.tail = list.head;                                                                                                                                                                            
            list.head->data = val;                                                                                                                                                                             
            list.head->prev = NULL;                                                                                                                                                                            
            list.head->next = NULL;                                                                                                                                                                            
            list.count = 1;                                                                                                                                                                                                                                                                                                                                                                                          
        } 
        else {                                                                                                                                                                                               
            Node *temp = (Node *)malloc(sizeof(Node));                                                                                                                                                         
            temp->data = val;                                                                                                                                                                                  
            temp->next = NULL;                                                                                                                                                                                 
            temp->prev = list.tail;                                                                                                                                                                           
            list.tail->next = temp;                                                                                                                                                                           
            list.tail = temp;                                                                                                                                                                                  
            list.count++;                                                                                                                                                                                      
        }                                                                                                                                                                                                      
    }                                                                                                                                                                                                          

    //close file pointer
    fclose(fp);
    // whhile loop repeats the code until user ends it 
    int reverse = 1;                                                                                                                                                                                              
    int choice = 0;                                                                                                                                                                                            
    while (choice != 12) {
        //print options                                                                                                                                                                                     
        printf("\n\n");                                                                                                                                                                                        
        printf("1. Display all nodes\n");                                                                                                                                                                      
        printf("2. Display nth node\n");                                                                                                                                                                      
        printf("3. Append a new node - Head or Tail? (H/T)\n");                                                                                                                                               
        printf("4. Append a new node in the Nth position\n");                                                                                                                                                  
        printf("5. Delete a node - Head or Tail? (H/T)\n");                                                                                                                                                    
        printf("6. Delete Nth node\n");                                                                                                                                                                        
        printf("7. Find a node\n");                                                                                                                                                                           
        printf("8. Get number of nodes\n");                                                                                                                                                                   
        printf("9. Display even numbered nodes\n");                                                                                                                                                            
        printf("10. Display odd numbered nodes\n");                                                                                                                                                            
        printf("11. Reverse list\n");                                                                                                                                                                          
        printf("12. Exit\n");                                                                                                                                                                                  
        printf("Enter choice: ");                                                                                                                                                                             
        scanf("%d", &choice);

        // switch statement for deciding what to run bassed on user input                                                                                                                                                                                  
        switch (choice) {                                                                                                                                                                                      
            case 1:                                                                                                                                                                                            
                displayAll(&list);                                                                                                                                                                             
                break;                                                                                                                                                                                        
            case 2:                                                                                                                                                                                           
                displayNth(&list);                                                                                                                                                                             
                break;                                                                                                                                                                                         
            case 3:                                                                                                                                                                                            
                appendHeadOrTail(&list,reverse);                                                                                                                                                                       
                break;                                                                                                                                                                                       
            case 4:                                                                                                                                                                                            
                appendNthPosition(&list);                                                                                                                                                                      
                break;                                                                                                                                                                                         
            case 5:                                                                                                                                                                                            
                deleteHeadOrTail(&list);                                                                                                                                                                      
                break;                                                                                                                                                                                         
            case 6:                                                                                                                                                                                            
                deleteNthNode(&list);                                                                                                                                                                          
                break;                                                                                                                                                                                         
            case 7:                                                                                                                                                                                           
                find(&list);                                                                                                                                                                                  
                break;                                                                                                                                                                                         
            case 8:                                                                                                                                                                                            
                getNumberOfNodes(&list);                                                                                                                                                                       
                break;                                                                                                                                                                                         
            case 9:                                                                                                                                                                                           
                displayEven(&list);                                                                                                                                                                            
                break;                                                                                                                                                                                         
            case 10:                                                                                                                                                                                           
                displayOdd(&list);                                                                                                                                                                             
                break;                                                                                                                                                                                        
            case 11:                                                                                                                                                                                          
                reverseList(&list);
                reverse = reverse*(-1);                                                                                                                                                                            
                break;                                                                                                                                                                                         
            case 12:                                                                                                                                                                                           
                printf("Goodbye!\n");                                                                                                                                                                         
                break;                                                                                                                                                                                        
        }                                                                                                                                                                                                      
   }
        //run destroy list to clear leaked memory                                                                                                                                                                                                                                                                                                                                                                                                                         
        destroyList(&list);                                                                                                                                                                                                                                                                                                                                                                                                  
        return 0;                                                                                                                                                                                              
}   