# Solution for the problem "Number Groups"
# https://www.hackerrank.com/contests/101hack52/challenges/number-groups

# Reading input value k
inValue = int(input().strip())

# The numbers in the k-th group are
# for even values of k ..., k^2 - 4, k^2 - 2, k^2, k^2 + 2, k^2 + 4,....
# for odd values of k ..., k^2 - 3, k^2 - 1, k^2 + 1, k^2 + 3, ...
# each group having k terms
# Cancelling the constant values from both sides since they have positive and negative signs
# effectivaly the sum of values in the k-th group is k ^ 3

# inValue raised to 3
outValue = pow(inValue, 3)

print(outValue)
