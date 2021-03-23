#approach first using pre defin function

from collections import OrderedDict
def duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(duplicate("Hello world"))
print(duplicate("My name is Alexmaxwell"))
print(duplicate("aaccabaa"))

#approach two  using string operation 

String=input("Enter the string")
result=''
for character in String:
    if character not in result:
        result +=character
print("your string",String)
print("After removing duplicate character",result) 