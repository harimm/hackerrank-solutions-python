def is_kaprekar(num):
    str_sqr = str(num * num)
    mid = len(str_sqr) // 2
    # Do not split if square has only one digit, else split at the middle
    sum_nums = int(str_sqr) if mid == 0 else sum(map(int, [str_sqr[:mid], str_sqr[mid:]]))
    # Check if original number and sum of split of square is same
    return num == sum_nums

lower_limit = int(input())
upper_limit = int(input())

kaprekar_nums = []
for i in range(lower_limit, upper_limit + 1):
    if is_kaprekar(i):
        kaprekar_nums.append(i)

if len(kaprekar_nums) > 0:
    print(' '.join(map(str, kaprekar_nums)))
else:
    print('INVALID RANGE')