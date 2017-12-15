# Solution for problem "Counting Valleys"
# https://www.hackerrank.com/challenges/counting-valleys/problem

# Number of steps taken
stepCount = int(input())
# Walk is a sequence of characters where 'U' denotes a step up and 'D' a step down
walk = input().strip()

# Current level
level = 0

# Valleys visited
valleys = 0

for step in walk:
    # For up, we increment the level and for down we decrement the level
    if step == 'U':
        level = level + 1
    else:
        # Every valley is a step from level 0 to a lower level
        if level == 0:
            valleys = valleys + 1
        level = level - 1

print(valleys)
