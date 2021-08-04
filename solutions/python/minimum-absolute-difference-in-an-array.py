# Solution for hackerrank problem "Minimum Absolute Difference in an Array"
# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

n = int(input())
nums = sorted(map(int, input().strip().split(' ')))

mindiff = abs(nums[0] - nums[1])

for i in range(1, n - 1):
    diff = abs(nums[i] - nums[i + 1])
    if diff < mindiff:
        mindiff = diff

print(mindiff)