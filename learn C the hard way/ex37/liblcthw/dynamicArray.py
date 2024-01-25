# !/usr/bin/python3
# -* coding: utf-8 -*-
# @author:xiaojiao

class DArray:
    """A dynamic array class akin to a simplified Python list."""
    
    def __init__(self, default_capacity = 10):
        self.capacity = default_capacity
        self.bucket = [None] * self.capacity
        self.expand_rate = 100
        self.count = 0
        self.max = 100
    
    def __getitem__(self, index):
        return self.bucket[index]
    
    def __setitem__(self, index, value):
        self.bucket[index] = value
    
    def push(self, element):
        if (self.count == self.capacity):
            self._expand()
        # self.bucket.append(element)
        # self.__setitem__(self.count, element)
        self.bucket[self.count] = element
        self.count += 1
    
    def pop(self):
        element = self.bucket[self.count - 1]
        self.count -= 1
        return element
    
    def destory(self):
        self.bucket = []
        self.count = 0
    
    def _expand(self):
        new_capacity = self.capacity * 2
        new_list = [None] * new_capacity
        for i in range(self.count):
            # copy list
            new_list[i] = self.bucket[i]
        self.capacity = new_capacity
        self.bucket = new_list
            
    
class MyClass:
    
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        print("setitem")
        self.data[index] = value
        
    def __delitem__(self, key):
        print("Call function __delitem__")
        del self.data[key]
    
obj = MyClass([1, 2, 3])   
obj[10] = 4
# arr = DArray()
# print(arr.capacity) # 10
# print(arr.count) # 0    



# arr = DArray()
# for i in range(10):
#     arr.push(i)
# print(arr.bucket) # [0, 1, 2, ..., 9]

# # expand

# arr = DArray(2)  
# for i in range(4):
#     arr.push(i)
# print(arr.capacity) # 4

# # set element
# arr = DArray()
# arr.push(1)
# print(arr[0]) # 1

# # pop element
# arr = DArray()
# arr.push(1)
# arr.push(2)  
# print(arr.pop()) # 2

# # iterate elements
# arr = DArray()
# for i in range(3):
#     arr.push(i)
# for item in arr.bucket:
#     print(item)