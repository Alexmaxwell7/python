lower=100
upper=1000

print("lowest numer",lower,"upper",upper)

for num in range(lower,upper+1):
    if num>1:
        for i in(2, num):
            if (num % i)==0:
                break
            else:
                print(num)