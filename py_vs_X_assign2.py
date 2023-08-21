"""
<INSERT YOUR NAME HERE>
"""

import time
import random
import math
import sys
sys.setrecursionlimit(500000)


def bubbleSort(list_of_items):
    start_time = time.time()

    # IF YOU CHOSE BUBBLE SORT, THEN COPY AND PASTE YOUR CODE FROM ASSIGN 2 HERE
    # NOTE: DON'T CHOOSE BUBBLE SORT UNLESS YOU A REASONABLY FAST MACHINE

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def mergeSort(list_of_items):
    start_time = time.time()

    # IF YOU CHOSE MERGE SORT, THEN COPY AND PASTE YOUR CODE FROM ASSIGN 2 HERE,
    # AND COPY ANY AUXILIARY FUNCTIONS YOU HAVE INTO THIS FILE AS WELL

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def quickSort(list_of_items):
    start_time = time.time()

    # IF YOU CHOSE QUICK SORT, THEN COPY AND PASTE YOUR CODE FROM ASSIGN 2 HERE,
    # AND COPY ANY AUXILIARY FUNCTIONS YOU HAVE INTO THIS FILE AS WELL

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def radixSort(list_of_items, max_digits):
    start_time = time.time()

    # IF YOU CHOSE RADIX SORT, THEN COPY AND PASTE YOUR CODE FROM ASSIGN 2 HERE,
    # AND COPY ANY AUXILIARY FUNCTIONS YOU HAVE INTO THIS FILE AS WELL

    elapsed_time = time.time() - start_time
    return (list_of_items, elapsed_time)


def assign02_main():
    with open('py_vs_X_assign2.txt') as f:
        list0 = [int(line.rstrip('\n')) for line in f]

    list1 = list(list0)
    list2 = list(list1)
    list3 = list(list1)

    # run sorting functions
    bubbleRes = bubbleSort(list0)
    print("done w/ bubble, list0[:10] = ", list0[:10])
    print("done w/ merge, list1[:10] = ", list1[:10])
    mergeRes2 = mergeSort(list1)
    print("done w/ merge, list1[:10] = ", list1[:10])
    print("done w/ merge, list2[:10] = ", list2[:10])
    quickResA = quickSort(list2)
    print("done w/ quick, list2[:10] = ", list2[:10])
    print("done w/ radix, list3[:10] = ", list3[:10])
    radixRes = radixSort(list3, math.ceil(math.log10(max(list3))))
    print("done w/ radix, list3[:10] = ", list3[:10])

    # Print results
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])

# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()
