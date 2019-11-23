
##iterators
def sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                temp= a[j]
                a[j]=a[j+1]
                a[j+1]=temp

a = [36,6,8,5444,6,69]
sort(a)
print (a)

#it = iter(a)
#print(it.__next__())