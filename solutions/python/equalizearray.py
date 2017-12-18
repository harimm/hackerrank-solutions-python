# Solution for the problem "Equalize the Array"
# https://www.hackerrank.com/challenges/equality-in-a-array/problem

# Number of values
numValues = int(input().strip())

# Reading n values into the list
valuesList = list(map(int, input().strip().split(' ')))

# Dictionary to hold count of each value
countValues = {}

# Iterate over the values to get the count on distinct items
for val in valuesList:
    # Read count from dictionary
    currentCount = countValues.get(val)

    # In case value doesnt exist, set it to one
    if currentCount == None:
        currentCount = 1
    # Otherwise increment the value
    else:
        currentCount = currentCount + 1

    # Put value into dictionary
    countValues[val] = currentCount

# To find minimum number of deletions, we need to find maximum count and delete from total count of values
numDeletions = numValues - max(countValues.values())

print(numDeletions)