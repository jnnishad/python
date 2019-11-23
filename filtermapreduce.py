import functools

lst = [23,35,8,96,41,53,9,48,934,3949,49,10,14,]
filt = list(filter(lambda a: a%2==0,lst))

print(filt)

task = list(map(lambda a: a+10 ,lst))
print(task)