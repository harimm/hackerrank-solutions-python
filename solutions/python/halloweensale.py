#!/bin/python3

def howManyGames(p, d, m, s):
    count = 0
    temp_cost = p
    current_cost = p
    # Return the number of games you can buy
    while temp_cost <= s:
        count += 1
        current_cost = max(current_cost - d, m)
        temp_cost += current_cost
    return count


p, d, m, s = map(int, input().strip().split(' '))
answer = howManyGames(p, d, m, s)
print(answer)
