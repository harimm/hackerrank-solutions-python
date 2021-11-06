def create_indexed_dict(nums):
    d = {}
    l = len(nums)
    for _ in range(l):
        num = nums[_]
        if num not in d.keys():
            d[num] = []
        d[num].append(_)
    return d


def get_indexes(d, num, index):
    if num in d.keys():
        return [x for x in d[num] if x > index]
    return []


def get_count_greater_than(arr, val):
    l = len(arr)
    index = 0
    while index < l:
        if arr[index] > val:
            break
        index += 1
    return l - index


def count_triplets(nums, n, r):
    d = create_indexed_dict(nums)
    count = 0
    for _ in range(n - 2):
        n1 = nums[_]
        n2 = n1 * r
        n3 = n2 * r
        indexes_2 = get_indexes(d, n2, _)
        if len(indexes_2) == 0:
            continue
        indexes_3 = get_indexes(d, n3, indexes_2[0])
        if len(indexes_3) == 0:
            continue
        for index2 in indexes_2:
            count_indexes_greater = get_count_greater_than(indexes_3, index2)
            if count_indexes_greater == 0:
                break
            count += count_indexes_greater
    return count


n, r = map(int, input().strip().split(' '))
nums = list(map(int, input().strip().split(' ')))
print(count_triplets(nums, n, r))
