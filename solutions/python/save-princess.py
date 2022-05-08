#!/usr/bin/python

# Find where the player is
def find_player_index(n, grid):
    for _ in range(0, n):
        for __ in range(0, n):
            if grid[_][__] == 'm':
                return _, __

# Find where the princess is
# Shortcut - Only need to check the 4 corners
def find_princess_index(n, grid):
    for _ in [0, n - 1]:
        for __ in [0, n - 1]:
            if grid[_][__] == 'p':
                return _, __


# Find player position
# Find princess position
# Determine moves based on relative postions
def displayPathtoPrincess(n, grid):
    player_index = find_player_index(n, grid)
    princess_index = find_princess_index(n, grid)

    # Find moves in vertical axis
    if player_index[0] > princess_index[0]:
        for _ in range(0, player_index[0] - princess_index[0]):
            print('UP')
    else:
        for _ in range(0, princess_index[0] - player_index[0]):
            print('DOWN')

    # Find moves in horizontal axis
    if player_index[1] > princess_index[1]:
        for _ in range(0, player_index[1] - princess_index[1]):
            print('LEFT')
    else:
        for _ in range(0, princess_index[1] - player_index[1]):
            print('RIGHT')


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)