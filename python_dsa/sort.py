
a=[92,54,34,87,56]
c=len(a)
for i in range(0,c-1):
    print(a[i])
    for j in range(1,c-1):
        print(a[j])
        if a[i] > a[j]:
            temp = a[i]
            a[i]=a[j]
            a[j]= temp
print(a)


a=[10,92,54,34,87,56]
b=[]
for i in range(len(a)-1):
    for j in range(1,len(a)):
        if (a[j]>a[i]):
            a[j],a[i]=a[i],a[j]
print(a)

a=[10,92,54,34,87,56]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
j=min(a)
print(j)

b=["asadasd","gd","zry","uuww"]
b.sort()
print(b)
b.sort(key=len)
print(b)

a=[23,43,54,967,808,8]
min_index=a.index(min(a))
print(min_index)
a[0],a[min_index]=a[min_index],a[0]
print(a)



