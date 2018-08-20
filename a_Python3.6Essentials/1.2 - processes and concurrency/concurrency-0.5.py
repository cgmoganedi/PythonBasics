import multiprocessing
def func(pipe_end):
    pipe_end.send(['hello','world'])
    pipe_end.close()
parent_end, child_end = multiprocessing.Pipe()
proc1 = multiprocessing.Process(target=func, args=(child_end))
proc1.start()
print(parent_end.recv())
proc1.join()
