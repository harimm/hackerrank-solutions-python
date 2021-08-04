N = int(input())
counts = {}

for _ in range(N):
    s = input()
    # Add to the counts dictionary if word already exists, else initialize dictionary value to 1
    if s in counts.keys():
        counts[s] = counts[s] + 1
    else:
        counts[s] = 1

# Output number of unique words, and count of each words in the order in which they are initially encountered
print(len(counts))
print(' '.join([str(x) for x in counts.values()]))
