# Solution for the problem "The Salesman"
# https://www.hackerrank.com/contests/world-codesprint-12/challenges/the-salesman

# Approach we are taking is to find the maximum and minimum numbers and then find their difference

# Number of test cases
t = int(input())

for i in range(t):
    # No. of houses. We are not going to use this variable
    n = int(input())

    nums = map(int, input().strip().split(' '))

    # Compute max and min and get the difference
    maxV = max(nums)
    minV = min(nums)
    print(maxV - minV)