# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

from threading import Thread
import time

def scheduler(function, milliseconds):
    time.sleep(milliseconds/1000)
    return function()

def say():
    print('Hey!')

job = Thread(target = scheduler, args=(lambda: say(), 1000))
job.start()