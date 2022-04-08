

def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return False
    else:
        return True
 
# Driver Code
year = 2000
if(checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")

# OR
s=2000
if s%100 == 0:
    print("not leap year")
if s%4 ==0 or s%400 == 0 :
    print("leap year")

else : 
    print(" not a leap year")