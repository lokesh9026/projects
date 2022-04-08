# finnobic series

n=10
a=0
b=1
for j in range(0,10):
        print(a)
        tem = a + b
        a,b=b,tem ## swapping in one line
        
n=10
a=0
b=1
for j in range(0,10):
        print(a)
        tem=a
        a=b
        b = tem +a

