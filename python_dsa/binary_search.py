
a=[43,23,54,76,89.22,90,1]
a.sort()
print(a)

def binary (num):
    lh=0
    rh=len(a)-1
    mid_ind=0

    
    while ( lh <= rh):
        mid_ind = (lh+rh)//2
        # print(mid_ind)
        mid_val = a[mid_ind]
        # print(mid_val)

        if (num == mid_val) :
            
            return mid_ind
            
            
        if mid_val <= num :
            lh = mid_ind + 1

        else :
            rh = mid_ind - 1

    return -1

index = binary(43)
print(index)


a= lambda a,b:a*b

print(a(2,2))
g=set(['sdf','vbn'])
print(g)
