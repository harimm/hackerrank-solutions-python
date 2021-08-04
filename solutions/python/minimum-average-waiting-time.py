from heapq import heappop, heappush


N = int(input())
customers = []
for i in range(0, N):
    customers.append(tuple(map(int, input().split(' '))))
customers = sorted(customers)

work_queue = []
sum_wait_time = 0
current_time = 0

while customers or work_queue:
    while customers and customers[0][0] <= current_time:
        heappush(work_queue, customers.pop(0)[::-1])
    if work_queue:
        current_customer = heappop(work_queue)
        current_time += current_customer[0]
        sum_wait_time += current_time - current_customer[1]
    else:
        customer = customers.pop(0)[::-1]
        heappush(work_queue, customer)
        current_time = customer[1]

print(sum_wait_time // N)

import heapq