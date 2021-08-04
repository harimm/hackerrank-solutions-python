N = int(input())

start_index = 0
keys = []
counts = {}

for _ in range(0, N):
    s = input()
    if s in counts.keys():
        counts[s] = counts[s] + 1
    else:
        counts[s] = 1
        keys.append(s)

print(len(keys))
print(' '.join([str(counts[x]) for x in keys]))
