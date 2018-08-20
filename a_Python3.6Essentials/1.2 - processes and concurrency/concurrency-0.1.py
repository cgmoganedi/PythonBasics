import threading

def print_sum():
    print('The sum of 1 and 2 is 3')
my_thread = threading.Thread(target=print_sum)
my_thread.start()
