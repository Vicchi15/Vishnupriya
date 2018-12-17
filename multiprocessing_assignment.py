import os

from multiprocessing import Process, current_process, Array
 
from multiprocessing import Process, Lock
 
lock = Lock()
 
 
def doubler(item):
    lock.acquire()
    try:
        result = number ** 2
        proc_name = current_process().name
        print('{0} is squared to {1} by: {2}'.format(number, result, proc_name))
    finally:
        lock.release()
 

if __name__ == '__main__':
    numbers=[]
    for i in range(1,11):
        numbers.append(i)
    toShare = Array('i',10)
    procs = []
    proc = Process(target=doubler, args=(10,))
 
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
 
    
    for proc in procs:
        proc.join()
