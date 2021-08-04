#!/bin/python3

import heapq


def cookies(k, A):
    # Write your code here
    count = 0
    # Create a min-heap
    heapq.heapify(A)
    l = len(A)
    # Execute only if there are at least two elements
    while l > 1:
        # If top is at least the required minimum, no further updates are necessary
        if A[0] >= k:
            break
        # Get the minimum two elements (and double the second one)
        top1 = heapq.heappop(A)
        top2 = 2 * heapq.heappop(A)
        # Push the sum back to the heap
        heapq.heappush(A, top1 + top2)
        count += 1
        l -= 1
    # If the heap top element is at least the required minimum, then return top, else fail
    return count if A[0] >= k else -1


n, k = map(int, input().strip().split(' '))
A = list(map(int, input().rstrip().split()))
result = cookies(k, A)
print(result)
