#include "lcthw/list_algos.h"
#include "lcthw/dbg.h"

inline void ListNode_swap(ListNode *a, ListNode *b) {
    check(a != NULL, "Invalid ListNode.");
    check(b != NULL, "Invalid ListNode.");
    void *temp = a->value;
    a->value = b->value;
    b->value = temp;
error:
    printf("something wrong with Node or NULL Node");
}

int List_bubble_sort(List *list, List_compare cmp) {
    int sorted = 1;

    if (List_count(list) < 1) {
        return 0;               // already sorted
    }

    ListNode *cur = NULL;
    do {
        sorted = 1;
        // LIST_FOREACH(list, first, next, cur) {
        //     if (cur->next) {
        //         if (cmp(cur->value, cur->next->value) > 0) {
        //             ListNode_swap(cur, cur->next);
        //             sorted = 0;
        //         }
        //     }
        // }
        cur = list->first;
        while(cur->next) {
            if (cmp(cur->value, cur->next->value) > 0) {
                ListNode_swap(cur, cur->next);
                sorted = 0;
            }
            cur = cur->next;
        }
    } while(!sorted);

    return 0;
}

// int List_bubble_sort(List *list, List_compare cmp) {
//     if (List_count(list) < 1) {
//         return 0;  // 已经排序好了
//     }

//     int sorted = 0;
//     ListNode *cur = NULL;
//     ListNode *last_unsorted = list->first;
//     ListNode *last_swap = NULL;

//     while (!sorted) {
//         sorted = 1;
//         cur = list->first;
//         ListNode *prev = NULL; // 记录当前节点的前一个节点
//         while (cur && cur->next != last_swap) {
//             ListNode *next = cur->next; // 记录当前节点的下一个节点
//             if (cmp(cur->value, next->value) > 0) {
//                 // 直接交换节点指针
//                 if (prev) {
//                     prev->next = next;
//                 } else {
//                     list->first = next;
//                 }
//                 cur->next = next->next;
//                 next->next = cur;
//                 sorted = 0;
//                 last_unsorted = cur;
//             } else {
//                 prev = cur;
//                 cur = next;
//             }
//         }
//         last_swap = last_unsorted;
//     }

//     return 0;
// }

// int List_bubble_sort(List *list, List_compare cmp) {
//     int length = List_count(list);

//     ListNode *node = list->first;
//     int swapped = 0;
//     for (int j = 0; j < length; j++) {
        
//         for (int i = 0; i < length - j; i ++) {
//             if (cmp(node->value, node->next->value) > 0) {
//                 ListNode_swap(node, node->next);
//                 swapped = 1;
//             }
//             if (node->next) node = node->next;
//         }
//         if (swapped == 0) {
//             break;
//         }
//     }
//     return 0;
// }

// inline List *List_merge(List *left, List *right, List_compare cmp) {
//    List *result = List_create();
   
// 	void *val = NULL;
// 	// int i = 0, j = 0;
//    	while ((List_count(left) > 0) && (List_count(right) > 0)) {
//     	if (cmp(List_first(left) , List_first(right)) <= 0) {
//             // List_push(result, List_first(left));
//             // i += 1;
// 			val = List_shift(left);
//         } else {
//             // List_push(result, List_first(right));
//             // j += 1;    
// 			val = List_shift(right);        
//         }
// 		List_push(result, val);
//    	}


//     //  Add the remaining elements to the result array
//     while (List_count(left) > 0) {
//         // remove first node in left list
//         val = List_shift(left);
// 		List_push(result, val);
//     }
    
//     // right as well
//     while (List_count(right) > 0) {
//         // remove first node in left list
//         val = List_shift(right);
// 		List_push(result, val);
//     }

//     return result;
// }

// https://github.com/preslavmihaylov/learn-c-the-hard-way/blob/master/33.LinkedListAlgorithms/liblcthw/src/lcthw/list_algos.c

// List *List_merge_sort(List *array, List_compare cmp) {
//     if (List_count(array) <= 1) {
//         return array;
//     }

//     // Split the array
//     // int mid = List_count(array) / 2;

//     // List *left = List_create();
//     // List *right = List_create();
//     // LIST_FOREACH(array, first, next, cur) {
//     //     if (mid > 0) {
//     //         List_push(left, cur->value);
//     //     } else {
//     //         List_push(right, cur->value);
//     //     }
// 	// 	mid -= 1;
//     // }
//     List *left = List_split_by_mid(array);
//     List *right = array;

//     List *sort_left = List_merge_sort(left, cmp);
//     List *sort_right = List_merge_sort(right, cmp);

//     if (sort_left != left) List_destroy(left);
//     if (sort_right != right) List_destroy(right);
//     return List_merge(sort_left, sort_right, cmp);
// }

// https://github.com/preslavmihaylov/learn-c-the-hard-way/blob/master/33.LinkedListAlgorithms/liblcthw/src/lcthw/list_algos.c

List *List_merge_sort(List *list, List_compare cmp) {
    if (List_count(list) <= 1) return list;

    List *left = List_create();
    List *second = List_create();
    List *result = List_create();

    int i = 0;
    LIST_FOREACH(list, first, next, cur) {

        if (i < List_count(list) / 2) {
            List_push(left, cur->value);
        } else {
            List_push(second, cur->value);
        }

        i++;
    }

    left = List_merge_sort(left, cmp);
    second = List_merge_sort(second, cmp);
	
    ListNode *firstNode = left->first;
    ListNode *secondNode = second->first;
    while (firstNode != NULL && secondNode != NULL) {
        if (cmp(firstNode->value, secondNode->value) <= 0) {
            List_push(result, firstNode->value);
            firstNode = firstNode->next;
        } else {
            List_push(result, secondNode->value);
            secondNode = secondNode->next;
        }
    }

    while (firstNode != NULL) {
        List_push(result, firstNode->value);
        firstNode = firstNode->next;
    }
    
    while (secondNode != NULL){
        List_push(result, secondNode->value);
        secondNode = secondNode->next;
    }
	
	//printList("RESULT ARRAY: ", result);
    
    List_destroy(left);
    List_destroy(second);

	return result;
}

List *List_insert_sorted(List *list, void *value, List_compare cmp) {
    // list required sorted
    // check(is_sorted(list) == 0, "list is not sorted.");
    check(list != NULL, "Invalid list.");

    List *array = List_copy(list);
    List *result = NULL;

    ListNode *node = NULL;
	node = array->first;

    if (List_count(list) == 0) {
        List_push(array, value);
        return array;
    } 

    if (cmp(array->first->value, value) >= 0) {
        List_unshift(array, value);
        return array;
    }

    if (cmp(array->last->value, value) <= 0) {
        List_push(array, value);
        return array;
    }

    // if the length of list less than 2

     if (List_count(list) <= 3) {
        // result = List_copy(list);
        result = array;
        List_push(result, value);
        List_bubble_sort(result, cmp);
        return result;
    }  

    while (node) {
        if ((cmp(node->value, value) <= 0) && (cmp(node->next->value, value) >= 0)) {
            // split list into part two..
            ListNode *listafter = NULL;
            ListNode *listbefore = NULL;

            // init insertNode
            ListNode *newNode = calloc(1, sizeof(ListNode));
            check_mem(newNode);
            newNode->value = value;

            listafter = node->next;
            listbefore = node;
            // node->next = NULL;
            // node->next->prev = NULL;

            // join two part 
            // List_push(listbefore, value);

            // maybe test this function List_cat... (xiaojiao 2023/08/14)

            node->next = newNode;
            node->next->prev = newNode;
            newNode->prev = listbefore;
            newNode->next = listafter;

            result = array;
            // printf("result <<<<<<<<<<<<<<<<<<<<<%d>>>>>>>>>>>>>>>>>>>>>>>>>\n", List_count(result));
            result->count += 1;
            break;
        } 
        node = node->next;
    }
    result = array;

    return result;

error:
    return NULL;
}

// List *List_insert_sorted(List *list, void *value, List_compare cmp) {
//     List *result = List_copy(list);
//     List_push(result, value);
//     List_bubble_sort(result,  cmp);
// // error:
//     // return NULL;
//     return result;
// }