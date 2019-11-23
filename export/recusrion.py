from itertools import *
from functools import *
import sys

tab1 = int(input("range for recursion : "))
if tab1 == 1:
    print (tab1)

else:
    dat1 = 0
    dat2 = 1
    print (dat1)
    print (dat2)
    for  i in range(2,tab1):

        sum = dat1+ dat2
        print (sum)
        tot= sum + i
        print (tot)
        dat1 = dat2
        dat2 = sum