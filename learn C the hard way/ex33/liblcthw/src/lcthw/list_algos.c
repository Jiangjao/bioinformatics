#include "lcthw/list_algos.h"
#include "lcthw/dbg.h"

inline void ListNode_swap(ListNode *a, ListNode *b) {
    void *temp = a->value;
    a->value = b->value;
    b->value = temp;
}

int List_bubble_sort(List *list, List_compare cmp) {
    int sorted = 1;

    if (List_count(list) < 1) {
        return 0;               // already sorted
    }

    do {
        sorted = 1;
        LIST_FOREACH(list, first, next, cur) {
            if (cur->next) {
                if (cmp(cur->value, cur->next->value) > 0) {
                    ListNode_swap(cur, cur->next);
                    sorted = 0;
                }
            }
        }
    } while(!sorted);

    return 0;
}

inline List *List_merge(List *left, List *right, List_compare cmp) {
   List *result = List_create();
   
	void *val = NULL;
	// int i = 0, j = 0;
   	while ((List_count(left) > 0) && (List_count(right) > 0)) {
    	if (cmp(List_first(left) , List_first(right)) <= 0) {
            // List_push(result, List_first(left));
            // i += 1;
			val = List_shift(left);
        } else {
            // List_push(result, List_first(right));
            // j += 1;    
			val = List_shift(right);        
        }
		List_push(result, val);
   	}


    //  Add the remaining elements to the result array
    while (List_count(left) > 0) {
        // remove first node in left list
        val = List_shift(left);
		List_push(result, val);
    }
    
    // right as well
    while (List_count(right) > 0) {
        // remove first node in left list
        val = List_shift(right);
		List_push(result, val);
    }

    return result;
}

List *List_merge_sort(List *array, List_compare cmp) {
    if (List_count(array) <= 1) {
        return array;
    }

    // Split the array
    int mid = List_count(array) / 2;

    List *left = List_create();
    List *right = List_create();
    LIST_FOREACH(array, first, next, cur) {
        if (mid > 0) {
            List_push(left, cur->value);
        } else {
            List_push(right, cur->value);
        }
		mid -= 1;
    }

    List *sort_left = List_merge_sort(left, cmp);
    List *sort_right = List_merge_sort(right, cmp);

    if (sort_left != left) List_destroy(left);
    if (sort_right != right) List_destroy(right);
    return List_merge(sort_left, sort_right, cmp);
}
