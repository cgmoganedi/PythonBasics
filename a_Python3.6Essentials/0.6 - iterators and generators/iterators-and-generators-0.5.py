def squares(value = 0):
    while True:
        value += 1
        yield (value - 1) * (value - 1)
        
generator = squares()

for i in range(5):
    print(next(generator))
