a=6
res=0
for i in range(1,6):
    if a%i == 0:
        res = res + i
if res == a :
    print("no is perfect")
else :
    print("no is not perfect")

## 6=1+2+3 , 1,2,3 are the divisors of 6