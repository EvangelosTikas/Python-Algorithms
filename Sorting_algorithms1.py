"""Implementing various algorithms for sorting and searching

#Example 1 two Python functions to find the minimum number on a list
The first utilizes O(n^2), sqaure_min(item) and the second one O(n) linear lin_min(item), checking the time for each algorithm
 """
__author__= "Vaggelis Tikas"

from random import randrange
from random import randint
from timeit import repeat
import timeit
ARRAY_LENGTH = 1000

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm} "\
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
def square_min(item):
    overallmin = item[0]
    for i in item:
        issmallest = True
        for j in item:
            if i>j:
                issmallest =False
                min =j
        if issmallest:
            overallmin = i

    return overallmin

def lin_min(item,s=0):
    min=item[0]
    for i in item:
        if i<min:
            min = i

    return min

# listsize1 = input("Give the listsize:") #coding driver
# blist=[]
# for i in blist:
#     blist[i]=input("Give the {} element".format(i))
#
# print(blist)

#print(square_min(blist))
#print(lin_min(blist))

"""
Compare the time between these algorithms
"""
#if __name__ == "__main__":
def Example1():
    print("Searching via O[n^2] function in python")
    for listsize in range(1000,5001,1000):
        alist = [randrange(100000) for x in range(listsize)]
        run_sorting_algorithm(algorithm ="square_min", array=alist)
        # start = timeit.timeit() ## another method for counting time in python ## different implementation of time measurements
        # print("Min: ",square_min(alist))
        # end = timeit.timeit()
        # print("size: %d time: %f"% (listsize, end - start))

    print("Searching via O[n] function in python")
    for listsize in range(1000,5001,1000):
        alist = [randrange(100000) for x in range(listsize)]

        print("Min: ",lin_min(alist))
        run_sorting_algorithm(algorithm="lin_min", array=alist)

## Example 2: Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
# Can you improve the algorithm from the previous problem to be linear? Explain.

def function1_ksmallest(item,k):
    n = len(item)
    for i in range(n):
        mid = (n)/2
        low = 0
        high = n-1
        while(low<=mid or high>=mid):
            if(item[low]>item[low+1]):
                item[low],item[low+1]=item[low+1], item[low]
            if(item[high-1]>item[high]):
                item[high],item[high-1]=item[high-1], item[high]
            low+=1
            high-=1
    return item[k-1]
def function2(item,k):
    n=len(item)
    low = 0
    high = n - 1
    mid=n/2
    while (low <= mid or high >= mid):
        if (item[low] > item[low + 1]):
            item[low], item[low + 1] = item[low + 1], item[low]
        if (item[high - 1] > item[high]):
            item[high], item[high - 1] = item[high - 1], item[high]

        low += 1
        high -= 1
    return item[k-1]

if __name__ == "__m__":
    array1 = [4,8,2,9,4,12,7,18]
    k=input("Give the k for the kth smallest element ") # Test function1 and function 2 for time complexity
    start = timeit.timeit()                             # Expected O(n^2) for function1_ksmallest
    print("Kth smallest number is: ", function1_ksmallest(array1, int(k)), " with time complexity O(n*logn)")
    end = timeit.timeit()
    print("size: %d time: %f"% (8, abs(end-start)))
    start2 = timeit.timeit()                            # Expected O(n) for function2 (less time)
    print("Kth smallest number is: ", function2(array1, int(k)), " with time complexity O(n)")
    end2 = timeit.timeit()
    print("size: %d time: %f" % (8, abs(end2 - start2)))
    Example1()                                          # Test sqaure and linear searching


# Example3: Python3 program to find k'th smallest element
# using min heap

# Class for Min Heap
class MinHeap:

    # Constructor
    def __init__(self, a, size):

        # list of elements in the heap
        self.harr = a

        # maximum possible size of min heap
        self.capacity = None

        # current number of elements in min heap
        self.heap_size = size

        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # Returns minimum
    def getMin(self):
        return self.harr[0]

    # Method to remove minimum element (or root)
    # from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")

        # Store the minimum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item
        # to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root

    # A recursive method to heapify a subtree with root at
    # given index. This method assumes that the subtrees
    # are already heapified
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if ((l < self.heap_size) and
                (self.harr[l] < self.harr[i])):
            smallest = l
        if ((r < self.heap_size) and
                (self.harr[r] < self.harr[smallest])):
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = (
                self.harr[smallest], self.harr[i])
            self.minHeapify(smallest)



#return k'th smallest element in a given array
def kthSmallest(arr, n, k):
    # Build a heap of n elements in O(n) time
    mh = MinHeap(arr, n)

    # Do extract min (k-1) times
    for i in range(k - 1):
        mh.extractMin()

    # Return root
    return mh.getMin()

# Driver code
if __name__== "__secondary__":
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print("K'th smallest element is", kthSmallest(arr, n, k))

#Example: 5 test and compare bubble sort, insertion_sort, merge_sort, quicksort, timsort
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):  # O(n^2)
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Loop from the element indicated by
    # `left` until the element indicated by `right`
    for i in range(left + 1, right + 1):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if the `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition `j` to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, position
        # the `key_item` in its correct location
        array[j + 1] = key_item

    return array

#implement quicksort
def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

# Implement timsort
def timsort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array

#Implement merge sort
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

if __name__ == "__main__":
    # Generate a sorted array of ARRAY_LENGTH items
    array = [i for i in range(ARRAY_LENGTH)]

    # Call each of the functions
    run_sorting_algorithm(algorithm="insertion_sort", array=array)
    run_sorting_algorithm(algorithm="merge_sort", array=array)
    run_sorting_algorithm(algorithm="quicksort", array=array)
    run_sorting_algorithm(algorithm="timsort", array=array)



