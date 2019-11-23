#force recursion to work like grep
#300058972165
import re, itertools
import PyQt
color = [ 'red', 'blue']
file = open('C:/Users/jaihinn00742/Desktop/python-3.7.2.post1-embed-amd64/300058972165.txt','r')
regex = re.compile(r"(\b300058972165\b)", re.I)
i = 0 ; output = "&lt;html&gt;"
for line in regex.finditer(file) :
    output += "".join([file[i:line.start()],
                       "&lt;strong&gt;&lt;span style='color:%s'&gt;" % color[line.lastindex-1],
                      file[line.start():line.end()],
                      "&lt;/span&gt;&lt;/strong&gt;"])
    i = line.end()
print ("".join([output, file[line.end():],"&lt;/html&gt;"]))
#for line in open('C:/Users/jaihinn00742/Desktop/python-3.7.2.post1-embed-amd64/300058972165.txt','r'):
#    if re.search('300058972165',line):
#        print(line)
                                 
#re


