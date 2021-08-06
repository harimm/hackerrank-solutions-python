n = int(input())
nums = list(map(int, input().strip().split(' ')))

# Have a dictionary to store last encountered index of each number
last_index_dict = {}
minimum_difference = -1

for i in range(n):
    num = nums[i]
    # If the number is already encountered,
    if num in last_index_dict.keys():
        # Find the last index
        last_index = last_index_dict[num]
        # Find the difference with the current index
        diff = i - last_index
        # If it is less than current available minimum of the minimum doesn't exist, update the minimum
        if minimum_difference == -1 or diff < minimum_difference:
            minimum_difference = diff
    # Update the index of the most recent encounter
    last_index_dict[num] = i

print(minimum_difference)