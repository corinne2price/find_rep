#!/usr/bin/env python3

oldpdb = open("sample.txt", 'r').read()


dic = {} #dictionary that will hold old and new names


with open("dict") as f: #dict = text file with old in col1 and new in col2
    for line in f:
       (old, new) = line.split()
       dic[(old)] = new

#print(dic)

for i, j in dic.items():
	print("replaced", i, "with",j)
	oldpdb = (oldpdb.replace(i, j))


open("replaced.txt", 'w').write(oldpdb)
