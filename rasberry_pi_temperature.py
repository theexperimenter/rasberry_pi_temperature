"""
Produces load on all available CPU cores
"""
from multiprocessing import Pool
from multiprocessing import cpu_count
import os
import time

def f(x):
    while True:
        x*x

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

if __name__ == '__main__':
    processes = cpu_count()
    print '-' * 20
    print 'Running load on CPU'
    print 'Utilizing %d cores' % processes
    print '-' * 20
    pool = Pool(processes)
    pool.map(f, range(processes))
    print(measure_temp())
    time.sleep(1)