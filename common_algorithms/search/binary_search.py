from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def binary_search(sorted_collection, target):
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        mid = int((right - left)/2)
        mid_point = sorted_collection[mid]
        if mid_point == target:
            return mid
        elif target < mid_point:
            right = mid_point - 1
        else:
            left = mid_point + 1
    return None
