# Solution for problem "Drawing Book"
# https://www.hackerrank.com/challenges/drawing-book/problem

# n number of pages
n = int(input())
# flip to page p
p = int(input())

# We need to flip the page x times to reach page 2x or 2x + 1
fromFront = int(p/2)
fromBack = n

oddPages = n % 2 == 1

if oddPages:
    # If number of pages are odd, last 2 pages can be viewed without flipping
    if p > n - 2:
        fromBack = 0
    # For other pages, we need to flip the page x times to reach page (n - p - 2x) or (n - p - (2x - 1))
    else:
        fromBack = int((n - p)/2)
# We need to flip the page x times for each page (n - p + 1 - 2x) or (n - p + 1 - (2x - 1))
else:
    fromBack = int((n - p + 1)/2)

print(min(fromFront, fromBack))

