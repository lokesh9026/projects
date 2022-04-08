a=[1,2,3,4,5,6]
print(a[::2])

# adding nos divisible by 2
b=[]
for i in a:
    if i%2 == 0:
        b.append(i)
print(b)
sumitem = sum(b)

print(sumitem)


# printing nos at even index which are divisible by 2
a=[1,2,3,4,5,9,10]
b=[]
for i in a[::2]:
    print(i)
    if i%2 == 0:
        b.append(i)
print(b)

# filter function to print even nos , it will return object

res=filter(lambda x:x%2==0 , range(1,11))
print(list(res))

# or
for i in range(11):
    if i%2==0:
        print(i)

