from functools import lru_cache
import time
@lru_cache(maxsize=None)  # This step is used for memoization ,you can also manage size by your own.
def fx(n):
    time.sleep(3)
    return n*5
print("4 x 5 =",fx(4))
print("5 x 5 =",fx(5))
print("6 x 5 =",fx(6))
# Before this step, every output is taking 3 secs but after that the remaining output will be displayed in less than 1 second because "lru_cache" has memoized the computation which is recently performed.
print("4 x 5 =",fx(4))
print("5 x 5 =",fx(5))
print("6 x 5 =",fx(6))