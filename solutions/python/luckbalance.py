# Solution for the problem "Luck Balance"
# https://www.hackerrank.com/challenges/luck-balance/

n, k = map(int, input().strip().split(' '))

luck = 0

important = []

for i in range(0, n):
    l, t = map(int, input().strip().split(' '))
    if t == 0:
        luck += l
    else:
        important.append(l)

important = sorted(important, reverse=True)

if (len(important) > k):
    luck -= (sum(important[k:]))
    important = important[:k]

luck += sum(important)

print(luck)