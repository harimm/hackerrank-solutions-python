# Solution for the problem "Cats and a mouse"
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

# Number of test cases
numQueries = int(input())

# Running the queries
for queryIndex in range(0, numQueries):
    # Locations of Cat A, Cat B and mouse
    locCatA, locCatB, locMouse = map(int, input().strip().split(' '))

    # Distance between Cat A and mouse
    distCatA = abs(locCatA - locMouse)
    # Distance between Cat B and mouse
    distCatB = abs(locCatB - locMouse)

    # Mouse escapes if both distances are equal
    if distCatA == distCatB:
        print("Mouse C")
    # Cat A is nearer
    elif distCatA < distCatB:
        print("Cat A")
    # Cat B is nearer
    else:
        print("Cat B")
