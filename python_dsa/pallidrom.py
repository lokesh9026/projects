i=161
test=161
res=0
while (i !=0 ):
    
    b=i%10
    res = res*10 + b
    i=i//10
    
print(res)

if test == res:
    print("no is pallidrom")
else :
    print("not a pallidrom no")

## second method by slicing 
n= str(i)
if n == n[::-1]:
    print("pallidrom no")