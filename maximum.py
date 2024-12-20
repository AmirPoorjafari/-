a=[10,9,8,7,6,5,4,3,2,1]
maximum=a[0]
for v in a[1:]:
    if(v>maximum):
        maximum=v

print(max(a))