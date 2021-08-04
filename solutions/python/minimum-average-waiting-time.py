from heapq import heappop, heappush


N = int(input())
customers = []
for _ in range(N):
    # customer[0] is arrival time, customer[1] is wait time
    customers.append(tuple(map(int, input().split(' '))))
# Sort by arrival time and then by wait time
customers = sorted(customers)

work_queue = []
sum_wait_time = 0
current_time = 0

# Execute if the customer list is not empty ot work queue is not empty
while customers or work_queue:
    # Loop to add all customers who have arrived at or before current time
    while customers and customers[0][0] <= current_time:
        # Add customer to work queue with the heap sorted using wait time (hence reversing the customer object)
        heappush(work_queue, customers.pop(0)[::-1])
    if work_queue:
        # If work queue is not empty, then get the customer with minimum wait time and serve him
        current_customer = heappop(work_queue)
        # Current time is updated by the adding the required wait time for serving
        current_time += current_customer[0]
        # Adding the total wait which the customer waited and add it to the sum
        sum_wait_time += current_time - current_customer[1]
    else:
        # If work queue is empty, then find the next customer who is arriving and add him to the work queue
        # If multiple customers arrive at the same time, then the one with the smaller wait time is taken
        # This order is maintained by the initial sort
        customer = customers.pop(0)[::-1]
        heappush(work_queue, customer)
        # Current time is updated to customers arrival time
        current_time = customer[1]

print(sum_wait_time // N)
