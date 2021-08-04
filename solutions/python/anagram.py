#!/bin/python3

o_a = ord('a')


def anagram(s):
    # If length of string is odd, we cannot split equally
    if len(s) % 2 == 1:
        return -1
    l = len(s) // 2

    # Split the input string
    s1, s2 = s[0:l], s[l:]
    # Initialize array to store count of each letter
    cs1, cs2 = [0] * 26, [0] * 26
    for _ in range(l):
        # Find the index of count array and update the counts
        ord_s1, ord_s2 = ord(s1[_]) - o_a, ord(s2[_]) - o_a
        cs1[ord_s1] += 1
        cs2[ord_s2] += 1

    # Find the sum of absolute differences and divide by 2 to find alphabets that need to be changed
    # If there are two letters that are different, we just need to change one, hence the division by two
    return sum([abs(cs1[x] - cs2[x]) for x in range(26)]) // 2


t = int(input())
for x in range(t):
    print(anagram(input().strip()))
