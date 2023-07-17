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









