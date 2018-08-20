import threading
sum1 = 0
my_lock = threading.Lock()

def adder():
    global sum1, my_lock
    my_lock.acquire(blocking=False)
    sum1 += 1
    my_lock.release()
my_thread = threading.thread(target=adder)
my_thread.start()
