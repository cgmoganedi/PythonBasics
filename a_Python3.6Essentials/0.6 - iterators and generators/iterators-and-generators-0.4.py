import itertools

even_list = list(itertools.filterfalse(lambda x: x%2, range(11)))
print(even_list)

print(list(filter( lambda y: (y+1)%2, range(11))))

