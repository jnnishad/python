#!/bin/python


import sys
import os
arg=int(sys.argv[1])
#print arg
for i in range(arg) :
	j=0
	while  j < i  :
	#	print i, j
		print '*',
		j=j+1
	print ''


