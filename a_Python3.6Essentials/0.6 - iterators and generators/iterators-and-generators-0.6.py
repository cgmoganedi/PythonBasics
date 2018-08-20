def up_down(value = 1):
    yield from range(1, value, 1)
    yield from range(value, 0, -1)

print(list(up_down(5)))

generator = up_down(4)

for i in range(7):
    print(next(generator))
