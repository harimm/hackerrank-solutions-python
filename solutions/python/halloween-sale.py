#!/bin/python3

def how_many_games(p, d, m, s):
    count = 0
    # Initialize current cost and starting cost to value of first item
    temp_cost = p
    current_cost = p
    # Return the number of games you can buy
    while temp_cost <= s:
        count += 1
        # Find the next cost by checking the maximum of newly calculated value and predefined minimum
        current_cost = max(current_cost - d, m)
        # Add the next cost to temporary total cost
        temp_cost += current_cost
    return count


p, d, m, s = map(int, input().strip().split(' '))
answer = how_many_games(p, d, m, s)
print(answer)
