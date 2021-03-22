mylist = [10,20,120,100,333,999]

num = int(input('enter the divison number'))

result=list(filter(lambda x:(x%num==0),mylist))


print("divisable by",num, "is",result)