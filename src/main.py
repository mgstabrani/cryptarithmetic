from function import *
import timeit
start = timeit.default_timer()
putLetters()
initNumber()
heapPermutation(list(range(10)),10,10)
stop = timeit.default_timer()
timeExecution = stop - start
print("Time Execution =", timeExecution, "second")