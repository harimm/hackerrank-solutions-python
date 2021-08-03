#!/bin/python3

o_a = ord('a')


def anagram(s):
    if len(s) % 2 == 1:
        return -1
    l = len(s) // 2

    s1, s2 = s[0:l], s[l:]
    cs1, cs2 = [0] * 26, [0] * 26
    for _ in range(l):
        ord_s1, ord_s2 = ord(s1[_]) - o_a, ord(s2[_]) - o_a
        cs1[ord_s1] += 1
        cs2[ord_s2] += 1

    return sum([abs(cs1[x] - cs2[x]) for x in range(26)]) // 2


t = int(input())
for x in range(t):
    print(anagram(input().strip()))
