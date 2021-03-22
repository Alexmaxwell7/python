values = input("enter the string")

reverse_string = values[::-1]

if reverse_string==values:
    print("palindrome")
else:
    print("not palindrome")
print (reverse_string)