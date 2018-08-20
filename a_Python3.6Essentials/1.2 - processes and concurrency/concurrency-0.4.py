import multiprocessing
def adder(a, b):
    return a + b
proc1 = multiprocessing.Process(target=adder, args=(2,2))
proc1.start()
proc1.join()
