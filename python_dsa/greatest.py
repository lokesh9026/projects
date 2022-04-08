# a=3,55,22
# b=list(a)
# c=max(b)
# print(c)

# s=min(b)
# print(s)


# sum =0
# for i in b:
#     sum = sum +i
# print(sum)



def add(i):
    if (i == 0):
        return 0
    else :
        sum = 0
        sum = sum + i%10
        return i//10
i=123
res=add(i)
print(res)

