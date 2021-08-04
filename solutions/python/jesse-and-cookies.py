#!/bin/python3

import heapq


def cookies(k, A):
    # Write your code here
    count = 0
    heapq.heapify(A)
    l = len(A)
    while l > 1:
        if A[0] >= k:
            break
        top1 = heapq.heappop(A)
        top2 = 2 * heapq.heappop(A)
        heapq.heappush(A, top1 + top2)
        count += 1
        l -= 1
    return count if A[0] >= k else -1


n, k = map(int, input().strip().split(' '))
A = list(map(int, input().rstrip().split()))
result = cookies(k, A)
print(result)
