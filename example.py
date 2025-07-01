a=[1,2,1,1,2,3,2,4,5,6,5,4,73,8,8,99,7,8,6,9]
n=len(a)
max=a[0]
for i in range(n):
    if(max<a[i]):
        max=a[i]
print(max)