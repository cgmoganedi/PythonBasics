import itertools as itt
accum = itt.accumulate(range(10))

for i in range(10):
    print(next(accum))

combin = list(itt.combinations(range(5), 2))

print(combin)
