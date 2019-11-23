
import os
import sys
import math
import re
#def connect(host='172.20.103.58', port='22', user='root', command='/bin/true')
process = ['File Appender','Database','mm_txn','exit','hii','hello']
for i in range(len(process)):
        #print str(i) + "..." + str(PROCESS(str((i)))
        print('\t\t\t\t\t\t\t' + str(i)+ ')' +  process[i])
spam=0
while spam <= 2 :
    print("inside loop " + str(spam))
    spam = spam+1
print('GOTTEN')

#arg=sys.argv[1]
data = "Reversal string : "
num = input(data)
size=len(num)
while size > 0 :

#for i in range(len(num)):
    size = size - 1
    print(num[size], end="")

