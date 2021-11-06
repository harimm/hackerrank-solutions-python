ORD_A = ord('a')


def init_dict():
    return [0] * 26


def increment_char(d, ch):
    index = ord(ch) - ORD_A
    d[index] = d[index] + 1


def decrement_char(d, ch):
    index = ord(ch) - ORD_A
    d[index] = d[index] - 1


def populate_word(d, w):
    for ch in w:
        increment_char(d, ch)


def check_words(d, d_):
    for _ in range(0, 26):
        if d[_] != d_[_]:
            return False
    return True


def sherlock_and_anagrams(s):
    l = len(s)
    pairs = 0
    for _l in range(1, l):
        d = init_dict()
        # Initialize to first word
        populate_word(d, s[0: _l])
        for i in range(0, l - _l):
            start_index = i + 1
            current_index = start_index
            d_ = init_dict()
            # Initialize to next word
            populate_word(d_, s[current_index:current_index + _l])
            while True:
                if check_words(d, d_):
                    pairs += 1
                current_index += 1
                if current_index > l - _l:
                    break
                decrement_char(d_, s[current_index - 1])
                increment_char(d_, s[current_index + _l - 1])
            decrement_char(d, s[i])
            increment_char(d, s[i + _l])
    return pairs


t = int(input())
for _ in range(t):
    s = input().strip()
    result = sherlock_and_anagrams(s)
    print(result)