import sched, time
def print_time():
    print(time.time())
my_sched = sched.scheduler()
my_sched.enter(10, 1, print_time)
