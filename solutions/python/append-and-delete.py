def is_string_possible(original, modified, changes):
    l_o, l_m = len(original), len(modified)
    # If there are more possible modifications than the total number of letters in
    # both strings, then that sequence of modifications is possible
    if changes >= l_o + l_m:
        return True

    l_check = min(l_o, l_m)
    same_letters = 0
    # Check how many starting letters are same in both strings
    for i in range(l_check):
        if original[i] != modified[i]:
            break
        same_letters += 1

    # actual count of different letters that need to be removed and added
    difference = l_o + l_m - 2 * same_letters

    # String is impossible if differences are greater or the difference between actual and required changes
    # are not a multiple of two
    if difference > changes or \
            (changes - difference) % 2 > 0:
        return False
    return True

if is_string_possible(input(), input(), int(input())):
    print("Yes")
else:
    print("No")
