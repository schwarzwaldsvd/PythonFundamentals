"""Task: Transform this simple sorting algorithm into a unique sort.
It should not return any duplicate values in the sorted array.

input: [1,5,2,1] => output: [1,2,5]
input: [4,2,2,3,2,2,2] => output: [2,3,4]

"""
import numpy as np

def unique_sort(arr):
    breadcrumbs = {}
    result = []

    for i, v in enumerate(arr):
        if v not in breadcrumbs:
            result.append(v)
            breadcrumbs[v] = i

    return np.sort(result)

print(unique_sort([4,2,2,3,2,2,2]))