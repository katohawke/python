#!/usr/bin/env python3

def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        guees = sorted_array[mid]
        if guees == item:
            return mid
        elif guees > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))
print(binary_search(my_list, -1))