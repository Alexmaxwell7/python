num1 = int(input("enter the first value"))
num2 = int (input('enter the second value'))

print("before swaping first value", num1)
print("before swaping second value", num2)

# approach one
# temp = num1
# num1 = num2
# num2 = temp 

# approach two 

num1,num2=num2,num1

print ('after the swaping first value',num1)
print ('after the swaping second value', num2)

