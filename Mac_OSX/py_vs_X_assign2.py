"""
Sarah Johnson
"""

import time
import random
import math
import sys
sys.setrecursionlimit(500000)


def bubbleSort(a_list):
    start_time = time.time()
    n = len(a_list)
    for i in range(n):
        for j in range(0, n - i - 1):
                if a_list[j] > a_list[j + 1]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    elapsed_time = time.time() - start_time
    return (a_list, elapsed_time)



def assign02_main():
    with open('py_vs_X_assign2.txt') as f:
        list0 = [int(line.rstrip('\n')) for line in f]

    list1 = list(list0)
    list2 = [5,3,6,7,1,]
    list3 = list(list1)

    # run sorting functions
    bubbleRes = bubbleSort(list0)
    #print("done w/ bubble, list0[:10] = ", list2[:10])


    # Print results
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])

# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()
