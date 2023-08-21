"""
<INSERT YOUR NAME HERE>
"""

import time


def linearSearch(list_of_items, item_sought):
    num_comparisons = 0
    item_found = False
    start_time = time.time()

    # IF YOU HAVE CHOSEN LINEAR SEARCH, THEN COPY AND PASTE YOUR ASSIGN 1 CODE HERE

    elapsed_time = time.time() - start_time
    return (item_found, num_comparisons, elapsed_time)


def binarySearch(list_of_items, item_sought):
    num_comparisons = 0
    item_found = False
    start_time = time.time()

    # IF YOU HAVE CHOSEN BINARYSEARCH, THEN COPY AND PASTE YOUR ASSIGN 1 CODE HERE

    elapsed_time = time.time() - start_time
    return (item_found, num_comparisons, elapsed_time)


def assign01_main():
    # load file to use as the list to search
    with open('py_vs_X_assign1.txt') as f:
        list1 = [int(line.rstrip('\n')) for line in f]

    item_to_find = 250999

    ls_res1 = linearSearch(list1, item_to_find)
    bs_res1 = binarySearch(list1, item_to_find)

    print(f"\nlist1 (size = {len(list1)}) results")
    if ls_res1[0]:
        print("  linear search found the item and required:")
    else:
        print("  linear search did not find the item and required:")
    print("   ", ls_res1[1], "comparisons")
    print(f"    {ls_res1[2]:.4f} seconds")

    if bs_res1[0]:
        print("  binary search found the item and required:")
    else:
        print("  binary search did not find the item and required:")
    print("   ", bs_res1[1], "comparisons")
    print(f"    {bs_res1[2]:.4f} seconds")


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign01_main()
