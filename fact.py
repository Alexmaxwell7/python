# fact = 1
# num = int(input('enter the fact value'))
# for i in range(1, num+1):
#     fact = fact * i
# print('The fact num', num , "is", fact)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * fact(n-1)

num = 5
print("fact of",num,"is",fact(num))
