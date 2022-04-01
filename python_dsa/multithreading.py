# multi threading (multi tasking)

import time
import threading
def square (num):
    for i in num :
        time.sleep(0.2)
        print(i*i)

def cube(num):
    for i in num:
        time.sleep(0.2)
        print(i*i*i)

t=time.time()
num=[2,3,4,5]
t1=threading.Thread(target= square , args=(num,))
t2=threading.Thread(target= cube , args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()
print( time.time()-t)


## iterators are like for loop
a=[4334,56,23,65]
i=iter(a)
print(next(i))
print(next(i))
print(next(i))

## genrators
## yield is like a return but it does not return in one short (one go) 
## use next
def test():
    yield "hi"
    yield "hello"
    

itr=test()

print(next(itr))
print(next(itr))

