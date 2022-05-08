#!/usr/bin/python

# Find where the princess is
def find_princess_index(n, grid):
    for _ in range(0, n):
        for __ in range(0, n):
            if grid[_][__] == 'p':
                return _, __


# Only find next move
def nextMove(n, r, c, grid):
    player_index = r, c
    princess_index = find_princess_index(n, grid)

    # Find moves in vertical axis
    if player_index[0] > princess_index[0]:
        return 'UP'
    elif player_index[0] < princess_index[0]:
        return 'DOWN'

    # Find moves in horizontal axis
    if player_index[1] > princess_index[1]:
        return 'LEFT'
    elif player_index[1] < princess_index[1]:
        return 'RIGHT'


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))