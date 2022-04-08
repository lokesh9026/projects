
for i in range(1001):
    num =i 
    res = 0
    n = len(str(i))
    while ( i != 0):
        j=i%10
        res = res+j**n
        i=i//10
    
    if num == res :
        print(num)