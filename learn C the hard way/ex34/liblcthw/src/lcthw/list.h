#include "dbg.h"
#ifndef lcthw_List_h
#define lcthw_List_h

#include <stdlib.h>

struct ListNode;

// A doubly linked list node
typedef struct ListNode {
    struct ListNode *next; // Pointer to the next node in the list
    struct ListNode *prev; // Pointer to the previous node in the list
    void *value;		   // Pointer to the value stored in the node
} ListNode;

// A doubly linked list
typedef struct List {
    int count;				// Number of nodes in the list
    ListNode *first;		// Pointer to the first node in the list
    ListNode *last;			// Pointer to the last node in the list
	// invariable
	#define ASSERT_COUNT_GE_ZERO(A) check((A)->count >= 0, "Count is negative.")
	#define ASSERT_FIRST_NOT_NULL(A) check(((A)->count == 0) || ((A)->first != NULL), "First is NULL with count >0.")
} List;

// Create, destroy, clear
List *List_create();
void List_destroy(List *list);
void List_clear(List *list);

// Remove all nodes from a list, and destroy the list itself
void List_clear_destroy(List *list);

// Get the number of nodes in a list
#define List_count(A) ((A)->count)
// Get the value stored in the first node of a list
#define List_first(A) ((A)->first != NULL ? (A)->first->value : NULL)
// Get the value stored in the last node of a list
#define List_last(A) ((A)->last != NULL ? (A)->last->value : NULL)

// Add, Revmove, Add a new node to the beginning of a list
void List_push(List *list, void *value);
void *List_pop(List *list);

void List_unshift(List *list, void *value);
void *List_shift(List *list);

// Remove a specific node from a list
void *List_remove(List *list, ListNode *node);


// Make a copy of the linked list
List *List_copy(List *list);

// Connect two linked lists
List *List_cat(List *list1, List *list2);

// Split list into 
List *List_split_by_mid(List *list);

//Macro for iterating over the nodes in a list
#define LIST_FOREACH(L, S, M, V) ListNode *_node = NULL;\
	ListNode *V = NULL;\
	for(V = _node = L->S; _node != NULL; V = _node = _node->M)


#endif // lcthw_List_h
