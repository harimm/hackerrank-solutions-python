initial_number = 3
current_number = 3
next_number = 3

# Need to simplify
def strange_counter():
    global current_number, initial_number, next_number
    if next_number == 0:
        initial_number *= 2
        next_number = initial_number
    current_number = next_number
    next_number -= 1
    yield current_number


cycle = int(input())
counter = strange_counter()

value = None
for _ in range(cycle):
    value = next(strange_counter())

print(value)