import multiprocessing
def func(queue1):
    queue1.put(['hello','world'])
    my_queue = multiprocessing.Queue()
    proc1 = multiprocessing.Process(traget=func, args=(my_queue,))
    proc1.start()
    print(my_queue.get())
    proc1.join()
