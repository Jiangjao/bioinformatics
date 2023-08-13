#include <stdlib.h>
#include "list.h"
#include "lcthw/dbg.h"
#include <assert.h>

List *List_create() {
	List *list = calloc(1, sizeof(List));
	
	// init list
	list->first = NULL;
	list->last = NULL;
	list->count = 0;
	ASSERT_COUNT_GE_ZERO(list);
	ASSERT_FIRST_NOT_NULL(list);
	return list;	    
error:
	free(list);
	return NULL; 
}

void List_destroy(List *list) {
	check(list != NULL, "Invalid list."); 
	LIST_FOREACH(list, first, next, cur) {
		if (cur->prev) {
			free(cur->prev);
		}
	}
	
	free(list->last);
	free(list);
error:
	return;
}

void List_clear(List *list) {
	check(list != NULL, "Invalid list."); 
	LIST_FOREACH(list, first, next, cur) {
		free(cur->value);
	}
error:
	return;
}

void List_clear_destroy(List *list) {
	check(list != NULL, "Invalid list."); 
	LIST_FOREACH(list, first, next, cur) {
		free(cur->value);
		if (cur->prev) {
			free(cur->prev);
		}
	}
	free(list->last);
	free(list);
	// List_clear(list);
	// List_destroy(list);
error:
	return;
}

int List_counts(List *list) {
	if (!list) return 0;
	return list->count;
}
	
void List_push(List *list, void *value) {
	check(list != NULL, "Invalid list."); 
	ListNode *node = calloc(1, sizeof(ListNode));
	check_mem(node);
	
	node->value = value;
	if (list->last == NULL) {
		list->first = node;
		list->last = node;
	} else {
		list->last->next = node;
		node->prev = list->last;
		list->last = node;
	}	

	list->count++;

error:
	return;
}

void *List_pop(List *list) {
	check(list != NULL, "Invalid list.");
	ListNode *node = list->last;
	return node != NULL ? List_remove(list, node) : NULL;
error:
	return NULL;
}

void List_unshift(List *list, void *value) {
	
	check(list != NULL, "Invalid list.");
	ListNode *node = calloc(1, sizeof(ListNode));
	check_mem(node);

	node->value = value;

	if (list->first == NULL) {
		list->first = node;
		list->last = node;
	} else {
		node->next = list->first;
		list->first->prev = node;
		list->first = node;
	}
	
	list->count++;

error:
	return;
}

void *List_shift(List *list) {
	check(list != NULL, "Invalid list.");
	ListNode *node = list->first;
	return node != NULL ? List_remove(list, node) : NULL;
error:
	return NULL;
}

void *List_remove(List *list, ListNode *node) {
	void *result = NULL;

	check(list != NULL, "Invalid list.");	
	check(list->first && list->last, "List is empty");
	check(node, "node can't be NULL");

	if (node == list->first && node == list->last) {
		list->first = NULL;
		list->last = NULL;
	} else if (node == list->first) {
		list->first = node->next;
		check(list->first != NULL, "Invalid list, somehow got a first that is NULL.");
		list->first->prev = NULL;
	} else if (node == list->last) {
		list->last = node->prev;
		check(list->last != NULL, "Invalid list, somehow got a next that is NULL.");
		list->last->next = NULL;
	} else {
		ListNode *after = node->next;
		ListNode *before = node->prev;
		after->prev = before;
		before->next = after;
	}

	list->count--;
	result = node->value;

error:
	return result;
}

List *List_copy(List *list) {
	check(list != NULL, "Invalid list.");
	List *list_dubp = List_create();
	list_dubp->first = list->first;
	
	LIST_FOREACH(list, first, next, cur) {
		List_push(list_dubp, cur->value);
    }
	return list_dubp;
error:
	return NULL;
}


List *List_cat(List *list1, List *list2) {
	check(list1 != NULL, "Invalid list.");
	check(list2 != NULL, "Invalid list.");
	
	List *list_dubp = List_copy(list1);

	LIST_FOREACH(list2, first, next, cur) {
		List_push(list_dubp, cur->value);	
	}

	return list_dubp;
error:
	return NULL;
}

ListNode **List_split_inplace(List *list, int boundary) {
	check(list != NULL, "Invalid list.");
	
	if ((list->count < 2) || (list->count >= boundary)) {
		// List *list_dubp = List_copy(list);
		// return &list_dubp;
		printf("List length less than 2\n");
		return NULL;
	}

	//List *list_new1 = List_create();
	//List *list_new2 = List_create();
	
	//LIST_FOREACH(list, first, next, cur) {
	//	if (list->count < boundary) {
	//		List_push(list_new1, cur->value);
	//	} else {
	//		List_push(list_new2, cur->value);
	//	}
	//}
	
	// replace with new splited-list
	// List_clear_destroy(list);
	// list = list_new1;	
	// return list_new2;
	ListNode *fast = list->first;

	for (int i = 0; i < boundary; i++) {
		fast = fast->next;
	}
	
	ListNode **result = (ListNode  **)malloc(2 * sizeof(ListNode *));
	result[0] = list->first;
	result[1] = fast->next;
	return result;
error:
	return NULL;
}

List *List_split_by_mid(List *list) {
	check(list != NULL, "Invalid list.");

	if (List_count(list) <= 1) {
		return NULL;
	}

	List *left =  List_create();
	// List *right = List_create();
	int mid = List_count(list) / 2;


	ListNode *node = NULL;
	node = list->first;
	
	while ((node->next != NULL) && (mid > 0)){
		List_push(left, node->value);
		node = node->next;
		List_pop(list);
		mid -= 1;
	}

	return left;

error:
	return NULL;
}
