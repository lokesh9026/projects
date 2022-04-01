a=[23,43,54,967,808,8]
for i in range(len(a)):
    min_val = min(a[i:])
    min_index=a.index((min_val))
    
    a[i],a[min_index]=a[min_index],a[i]
print(a)

##https://www.youtube.com/watch?v=nFG6pKhsUIY&list=PLzgPDYo_3xunyLTJlmoH8IAUvet4-Ka0y&index=2
a=[23,43,54,967,808,8]
for i in range(len(a)):
    max_val= max(a[i:])
    ind=a.index(max_val)
    a[i],a[ind]=a[ind],a[i]
print(a)


a=[23,43,23,54,967,808,8,23]
for i in range(len(a)):
    max_val= max(a[i:])
    ind=a.index(max_val)
    a[i],a[ind]=a[ind],a[i]
print(a)

