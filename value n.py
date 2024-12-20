import random



a=[10,20,30,40,50,60,70,80,90,100]
n=len(a)


for i in range(n //2 ):
    temp=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=temp

a=a[::-1]
print(n)