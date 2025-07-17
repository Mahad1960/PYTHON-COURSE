import threading
from concurrent.futures import ThreadPoolExecutor
import time
def fun(sec):
    print(f"Sleeping for {sec} seconds.")
    time.sleep(sec)
print("\n")
print("NORMAL CODE:")
# In this code, 1st function run then 2nd one run and at the end 3rd one run.
fun(4)
fun(3)
fun(2)
print("\n")
print("THREAD CODE:")
# In this code, every function start at the same time.
t1=threading.Thread(target=fun,args=[4])
t2=threading.Thread(target=fun,args=[3])
t3=threading.Thread(target=fun,args=[2])
t1.start()   # "Start" doesn't wait for the thread to finish. 
t2.start() 
t3.start()
t1.join()    # "Join" waits for the thread to finish.
t2.join()
t3.join()
# The following function allows you to run multiple functions.
# This method is much better than manually using "threading.Thread", "start", "join".
print("\n")
print("THREAD POOL EXECUTOR 1st METHOD:")
def demo1():
    with ThreadPoolExecutor() as executor:
        future=executor.submit(fun,3)  # You can call this multiple times.
        print("Specific Task Completion Msg:",future.result())  # This will print some msg when specific task completes.
        future=executor.submit(fun,2)  
        print("Specific Task Completion Msg:",future.result())
demo1()
print("\n")
print("THREAD POOL EXECUTOR 2nd METHOD:")
def demo2():
    with ThreadPoolExecutor() as executor:
        l=[2,3,4]
        result=executor.map(fun,l)    # This will send arguments to "fun" Function.
demo2()