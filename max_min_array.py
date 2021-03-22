arr = [20,40,10,100,5]

max = arr[0]

n = len(arr)

for i in range (1,n):
    if arr[i]>max:
        max= arr[i]
print('max of element', max)


min = arr[0]
n= len(arr)

for i in range (1,n):
    if arr[i]<min:
        min=arr[i]
print('min of element', arr[i])