
from heapq import merge

alist = [54, 26, 93, 17, 77, 31, 44, 88, 55, 20]
print("Unsorted list")
print(alist)

def my_bubbleSort(someList):

    for i in range(len(someList)-1, 0, -1):
        for x in range(i):
            if someList[x] > someList[x+1]:
                temp = someList[x]
                someList[x] = someList[x+1]
                someList[x+1] = temp

def insertion_sort(inputList):

    for i in range(1, len(inputList)):
        j = i - 1
        nxt_element = inputList[i]
        # Compare the current element with next one

        while (inputList[j] > nxt_element) and (j >= 0):
            inputList[j + 1] = inputList[j]
            j = j - 1
            inputList[j + 1] = nxt_element


def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


def merge_sort(alist):
    # print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    # print("Merging ",alist)



to_be_sorted = alist[:] #copy of the list
my_bubbleSort(to_be_sorted)
print("Bubble Sort:")
print(to_be_sorted)

to_be_sorted = alist[:] #copy of the list
insertion_sort(to_be_sorted)
print("Insertion Sort:")
print(to_be_sorted)

to_be_sorted = alist[:] #copy of the list
selection_sort(to_be_sorted)
print("Selection Sort:")
print(to_be_sorted)

to_be_sorted = alist[:] #copy of the list
merge_sort(to_be_sorted)
print("Merge Sort:")
print(to_be_sorted)

print(alist)

'''
A way to copy a list by value:

new_list = old_list[:]
If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

import copy
new_list = copy.deepcopy(old_list)
'''

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))

my_tuple = (20)
print(my_tuple)