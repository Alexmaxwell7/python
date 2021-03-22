mylist = ["max","alex","max"]

counter = 0

n = 2

word = "max"

for i in range(0,len(mylist)):
    if(mylist[i]==word):
        counter +=1
        if (counter == n):
            del mylist[i]

print(mylist)