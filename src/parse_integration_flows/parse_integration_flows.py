'''Finds deployed Integration flows starting with "XXL_"'
'Created on Mar 19, 2020'

@author: 08925
'''
import os,sys
import re
sorted_matches = []
num_args = len(sys.argv)
filename = sys.argv[1]
f = open(filename, 'r+')
my_file_data = f.read()
regex = r"^(XXL[A-Za-z0-9_ ]+).*Started.*$\n^Integration"
matches = re.finditer(regex, my_file_data, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
#        print ("{group}".format(group = match.group(groupNum)))
        sorted_matches.append(match.group(groupNum))
sorted_matches.sort()        
#print(sorted_matches)
for xmatch in sorted_matches:
    print(xmatch)
f.close