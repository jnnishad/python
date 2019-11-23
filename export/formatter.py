import os
import re

print(r"the elve's  got through the 'door'")
print(r"the elve's  got\n through the 'door'")


credit = [26, 65, 45, 44, 245]
credit.sort()
print(credit)

process = ['File Appender','Database','mm_txn','exit']
for i in range(len(process)):
        #print str(i) + "..." + str(PROCESS(str((i)))
        print('\t\t\t\t\t\t\t' + str(i)+ ')' +  process[i])

process.append('test')
process.pop(2)
process.append('mm_txn')
print(process)

#process.insert('init',0)
print(process)

pyhelp = help(sys,argv)
print('pyhelp')