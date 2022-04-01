dic={"name":"lokesh","mail":"jplk"}

print([(k, dic[k]) for k in dic])

for i in dic:
    print(dic[i])

# switch case is not there but we can do it by dictionary
def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
        return switcher.get(i,"Invalid day of week")

txt=week(5)
print(txt)