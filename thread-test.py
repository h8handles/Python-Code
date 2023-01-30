import timeit
import threading


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