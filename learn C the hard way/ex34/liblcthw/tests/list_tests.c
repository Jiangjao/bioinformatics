#include "minunit.h"
#include "lcthw/list.h"
#include <assert.h>

static List *list = NULL;
char *test1 = "test1 data";
char *test2 = "test2 data";
char *test3 = "test3 data";

char *test_create() {
	list = List_create();
	mu_assert(list != NULL, "Failed to create list.");
	
	return NULL;
}

char *test_destroy() {
	List_clear_destroy(list);
	
	return NULL;
}

char *test_push_pop() {
	List_push(list, test1);
	mu_assert(List_last(list) == test1, "Wrong last value.");

	List_push(list, test2);
	mu_assert(List_last(list) == test2, "Wrong last value.");

	List_push(list, test3);
	mu_assert(List_last(list) == test3, "Wrong last value.");
	mu_assert(List_count(list) == 3, "Wrong count on push.");

	char *val = List_pop(list);
	mu_assert(val == test3, "Wrong value on pop.");

	val = List_pop(list);
	mu_assert(val == test2, "Wrong value on pop.");

	val = List_pop(list);
	mu_assert(val == test1, "Wrong value on pop.");
	mu_assert(List_count(list) == 0, "Wrong count after pop.");

	return NULL;	
}

char *test_unshift() {
	List_unshift(list, test1);
	mu_assert(List_first(list) == test1, "Wrong first value.");
	
	List_unshift(list, test2);
	mu_assert(List_first(list) == test2, "Wrong first value.");

	List_unshift(list, test3);
	mu_assert(List_first(list) == test3, "Wrong last value.");
	mu_assert(List_count(list) == 3, "Wrong count on unshift.");

	return NULL;
}

char *test_remove() {
	// we only need to test the middle remove case since push/shift
	// already tests the other cases
	
	char *val = List_remove(list, list->first->next);
	mu_assert(val == test2, "Wrong removed element.");
	mu_assert(List_count(list) == 2, "Wrong count after remove.");
	mu_assert(List_first(list) == test3, "Wrong first after remove.");
	mu_assert(List_last(list) == test1, "Wrong last after remove.");

	return NULL;
}

char *test_shift() {
	mu_assert(List_count(list) != 0, "Wrong count before shift.");

	char *val = List_shift(list);
	mu_assert(val == test3, "Wrong value on shift.");

	val = List_shift(list);
	mu_assert(val == test1, "Wrong value on shift.");
	mu_assert(List_count(list) == 0, "Wrong count after shift.");

	return NULL;
}

char *test_list_dup() {
	List *list = List_create();
	List_push(list, test1);
	
	List *list1 = List_copy(list);
	mu_assert(List_first(list1) == test1, "Wrong first value after copying linked list.");
	mu_assert(List_last(list1) == test1, "Wrong last value after copying linked list.");
	
	mu_assert(List_count(list1) == 1, "Wrong count after copying linked list.");
	
	List_clear_destroy(list);
	return NULL;		
}

char *test_list_cat() {
	List *list1 = List_create();
	List *list2 = List_create();
		
	List_push(list1, test1);
	List_push(list2, test2);
	List *result = List_cat(list1, list2);

	mu_assert(List_first(result) == test1, "Wrong first value after connecting two linked list.");
	mu_assert(List_last(result) == test2, "Wrong last value after connecting two linked list.");	
	mu_assert(List_count(result) == 2, "Wrong count after connect two linked list.");
	
	// List_clear_destroy(list1);
	// List_clear_destroy(list2);

	return NULL;
}

char *test_list_split_by_mid() {
	List *list1 = List_create();
	List *list2 = List_create();
		
	List_push(list1, test1);
	List_push(list1, test2);
	List *result = List_split_by_mid(list1);
	mu_assert(List_first(result) == test1, "Wrong first value after spliting list.");
	mu_assert(List_count(result) == 1, "Wrong count after spliting list.");
	
	List_push(list1, test3);
	List *result2 = List_split_by_mid(list1);
	mu_assert(List_count(result2) == 1, "Wrong count after spliting list.");
	mu_assert(List_first(result2) == test1, "Wrong first value after connecting two linked list.");	

	List_push(list2, test1);
	List_push(list2, test2);
	List_push(list2, test3);
	List *result3 = List_split_by_mid(list2);
	mu_assert(List_count(result3) == 1, "Wrong count after spliting list.");
	mu_assert(List_first(result3) == test1, "Wrong first value after spliting list.");	

	// fixme(xiaojiao): turn on that , some errors... 2023/08/13
	// List_clear_destroy(list1);
	// List_clear_destroy(list2);
	// mu_assert(List_count(result2) == 2, "Wrong count after connect two linked list.");
	return NULL;
}


char *all_tests() {
	mu_suite_start();

	mu_run_test(test_create);
	mu_run_test(test_push_pop);
	mu_run_test(test_unshift);
	mu_run_test(test_remove);
	mu_run_test(test_shift);
	mu_run_test(test_destroy);

	mu_run_test(test_list_split_by_mid);
	mu_run_test(test_list_cat);
	return NULL;
}

RUN_TESTS(all_tests);
