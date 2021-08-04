# Solution for the problem "Constructing a Number"
# https://www.hackerrank.com/contests/hourrank-25/challenges/constructing-a-number/problem

# Number of test cases
t = int(input())

for x in range(t):
    # Number of items. We are not actually using this in our approach
    n = int(input())
    # We are replacing all spaces to get one big number
    num = int(input().replace(' ', ''))
    # Check whether number is divisible by 3
    print("Yes" if num % 3 == 0 else "No")