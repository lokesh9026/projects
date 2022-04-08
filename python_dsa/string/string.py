# # reverse the string
# a="tarun"
# j=""
# for i in a:
#     j = i + j
# print(j)


# t= list(a)
# t.sort()
# print(t)
# t.sort(reverse=True)
# print(t)


# # addition of string nos
# r="123"
# su=0
# for i in r:
#     if i.isdigit():
#         su=su +int(i)
# print(su)


# Print all repeated characters of a string in order 
a="tarrun"
l=len(a)
count=0
for i in range(l):
    for j in range(l):     
         if a[i] == a[j] and i !=j :
            count =count + 1
            break
print(count)

# Print all distinct characters of a string in order 
a="tarrun"
l=len(a)
count=0
for i in range(l):
    for j in range(l):     
         if a[i] != a[j] and i !=j :
            count =count + 1
            break
print(count)