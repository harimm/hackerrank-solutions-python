count = int(input())

name, max_count = '', 0
for i in range(0, count):
    values = input().strip().split(' ')
    diff = int(values[2]) - int(values[1])
    if diff > max_count:
        name = values[0]
        max_count = diff

print(name, max_count, sep=' ')