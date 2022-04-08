
# map fun take fun and sequence (list,tuple)
z=[2,4,6]
def square(n):
    return n**2
res=map( square,z)
print(list(res))

# lambda fun is like normal fun take arguments and expression: lambda( arguments : expression )
x=3
y=4
s=lambda x,y : x+y 
print(s(x,y))

j= lambda x,y : x*y
print(j(x,y))