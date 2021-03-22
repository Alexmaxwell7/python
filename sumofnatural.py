num =int(input("enthe your number"))
sum=0
if num<0:
    print("enter the postivie number")
else:
    while (num >0):
        sum+=num
        num -=1
print('the sum is',sum)