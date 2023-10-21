import math
example = [1, 3, 2, 5, 4, 9, 6, 10, 8, 7]

# 1. Split the array
# 2. Sort elements in two
# 3. Merge sub-arrays
# Merge Sort
def merge_split(array):
    length = len(array)
    if length == 0:
        return []
    if length > 0:
        left_length = math.ceil(length / 2)
        left = array[:left_length]
        right = array[left_length:]
        return left, right

def swap(a, b):
    temp = a
    a = b
    b = temp


# Merge arrays
def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array
    left = []
    right = []

    left_length = math.ceil(length / 2)
    left = array[:left_length]
    right = array[left_length:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while len(left) > 0:
        result.append(left[0])
        left.pop(0)

    while len(right) > 0:
        result.append(right[0])
        right.pop(0)

    return result

def merge_sort(array):
    if len(array) <= 1:
        return array

    # Split the array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort the left and right subarrays
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted left and right subarrays
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the sorted left and right subarrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements to the result array
    result += left[i:]
    result += right[j:]

    return result


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # flag, a remainder to swap
        swapped = False
        for j in range(n):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
    

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # flag, a remainder to swap
        swapped = False
        for j in range(n - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

# bracket.append(example.pop())
# print(merge_sort(example))

def radix_sort_v1(arr):
    """radix sort, element in array has to be positive integer

    Args:
        arr (list): postive integers

    Returns:
        arr (list): a list which elements in order
    """
    # Find the maximum value in the array to determine the number of digits
    max_value = max(arr)
    max_digits = len(str(abs(max_value)))

    # Perform radix sort
    for digit in range(max_digits):
        # Create 10 buckets (0 to 9)
        buckets = [[] for _ in range(10)]

        # Place elements into the corresponding buckets
        for num in arr:
            # Get the digit value at the current position
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)
        
        # Collect elements from the buckets
        # spread the bucket into one list which only contains integer
        arr = [num for bucket in buckets for num in bucket]
    
    return arr



def radix_sort_v2(arr):
    """radix sort, element in array has to be positive integer

    Args:
        arr (list): postive integers

    Returns:
        arr (list): a list which elements in order
    """
    # Find the maximum value in the array to determine the number of digits
    max_value = max(arr)
    max_digits = len(str(abs(max_value)))

    count = []
    
    # for digit in range(max_digits):
    #     digit_count = [0] * 10
    
    digit_count = [0] * 10
    # digit_count = [0] * max_digits
    # digit = 
    for num in arr:
        digit_value = (int)(math.log10(num))
        # print(digit_value) 
        digit_count[digit_value] += 1
        
    # print(digit_count)
    # Perform radix sort
    for digit in range(max_digits):
        # Create 10 buckets (0 to 9)
        buckets = [[] for _ in range(10)]

        # Place elements into the corresponding buckets
        for num in arr:
            # Get the digit value at the current position
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)
        
    
        # Collect elements from the buckets
        # spread the bucket into one list which only contains integer
        arr = [num for bucket in buckets for num in bucket]
        print(buckets)
    return arr

# Testing the code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort_v2(arr)
print(sorted_arr)
