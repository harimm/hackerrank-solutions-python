# Solution for the problem "Random Note"
# https://www.hackerrank.com/challenges/ctci-ransom-note/

def createDictionary(array):
    dictionary = {}
    for x in array:
        if x in dictionary.keys():
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary


input()
magazine = createDictionary(input().strip().split())
ransom_note = createDictionary(input().strip().split())

impossible = False

for k in ransom_note.keys():
    if k not in magazine.keys() or magazine[k] < ransom_note[k]:
        impossible = True
        break

if impossible:
    print("No")
else:
    print("Yes")

