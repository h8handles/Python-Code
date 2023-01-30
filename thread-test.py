import timeit
import threading

'''
Description: This snippet will output 100 values and time it with and without threading.
'''

def numbs():                                                                               
     for i in range(1,100):                                                               
             print(i)


def numbs_threaded():                                                                               
     for i in range(1,100):                                                               
             print(i)


thread = threading.Thread(target=numbs_threaded)
thread.start()




elapsed_time = timeit.timeit(numbs,number=1)
print(elapsed_time)
elapsed_time = timeit.timeit(numbs_threaded,number=1)
print(elapsed_time)
