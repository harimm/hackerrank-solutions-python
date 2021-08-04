# Solution for the problem "The Hurdle Race"
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

# Number of hurdles, and initial height that player is able to jump
hurdleCount, initialHeight = map(int, input().strip().split(' '))

# Heights of hurdles
hurdleHeights = list(map(int, input().strip().split(' ')))

# Maximum height of hurdles
maxHeight = max(hurdleHeights)

# Number of drinks needed initialized to zero
magicDrinkCount = 0

# If the maximum height is more than possible height, the number of drinks needed is the difference between
# maximum height and initial jumping height
if maxHeight > initialHeight:
    magicDrinkCount = maxHeight - initialHeight

print(magicDrinkCount)