import time
start_time = time.time()

import functions as funcs # type: ignore
from two_powers import fast2bin

n = 1000
a = fast2bin(n)
s = funcs.sum_digits(a)
print(a)
print(s)

print("--- %s seconds ---" % (time.time() - start_time))