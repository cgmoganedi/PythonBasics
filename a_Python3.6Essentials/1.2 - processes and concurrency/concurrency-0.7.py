import multiprocessing
def adder(a):
    return a+a
pool1 = multiprocessing.Pool(processes=4)

#this method blocks until all processes return
pool1.map(adder, range(10))

#this method returns a result object
results = pool1.map_async(adder, range(10))
results.wait()
