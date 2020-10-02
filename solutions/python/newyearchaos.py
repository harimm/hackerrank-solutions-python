# Solution for the problem "New Year Chaos"
# https://www.hackerrank.com/challenges/new-year-chaos/problem

t = int(input())

for i in range(0, t):
    n = int(input())
    positions = list(map(int, input().strip().split(' ')))

    gone_ahead = 0
    chaotic = False

    for index in range (0, n - 1):
        num = positions[index]

        diff = num - index - 1

        if diff > 2:
            chaotic = True
            break
        num_a = positions[index + 1]
        if num > num_a:
            gone_ahead += 1
            positions[index], positions[index + 1] = num_a, num

    if chaotic:
        print("Too chaotic")
        continue

    for index in range (n - 2, -1, -1):
        for index2 in range (0, index):
            num = positions[index2]

            diff = num - index2 - 1

            num_a = positions[index2 + 1]
            if num > num_a:
                gone_ahead += 1
                positions[index2], positions[index2 + 1] = num_a, num

    print(gone_ahead)