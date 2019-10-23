#!/bin/python
#_*_ coding: utf-8 _*_
import os
import sys
import json
import subprocess
import mysql.connector
from subprocess import *
#reload(sys)
#sys.setdefaultencoding("utf-8")


process = [ 'Search transaction','Processor','Memory','Space','Process','Time','exit' ]
for i in range(len(process)):
        #print str(i) + "..." + str(PROCESS(str((i)))
        print  ("\t\t\t\t\t\t\t" + str(i) + ')' + str(process[i]))

user='root'
passwd='Atom@123'
ip='localhost'
db='jai'
		
CNX = mysql.connector.connect(user=user,password=passwd,host=ip,database=db,buffered=True)
cursor = CNX.cursor()
query = ("select * from test_txn")
cursor.execute(query)
print cursor.fetchone()

#for (student_id, name, department) in cursor:
#	print(student_id,name,department)
#print ('NO','NAME','Department')
#########print cursor
#for i in cursor:
	#stringutf8 = u''.joins(string(i)).decode('utf-8')
	#print str(i)
	#print '[%s]' % ','.join(map(repr,i))

#cursor.close()
#CNX.close()

