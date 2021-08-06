n = int(input())
nums = list(map(int, input().strip().split(' ')))

count_breads = 0

# Only count until penultimate person
for i in range(n - 1):
    # If current person has even number of loaves, no need to give more
    if nums[i] % 2 == 0:
        continue
    # Give a bread to current and next person in line
    count_breads += 2
    nums[i] += 1
    nums[i + 1] += 1

# If last person has odd number of loaves, it is now impossible to distribute even number of loaves
if nums[-1] % 2 == 1:
    count_breads = 'NO'

print(count_breads)

