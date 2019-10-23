#!/bin/python

import os

path = (os.path.dirname(os.path.realpath(__file__)))

words = 'You know what this file could do ?'
words +=  '\nHAM'*50


for i in range(5):
        f=open('%03d_myfile.html'%i,'w')
        f.write(words)
        f.close

print('done!!!!')

