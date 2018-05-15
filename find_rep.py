#!/usr/bin/env python3
#Good for psf and pdb files (up to one replacement per line)

dic = {} #dictionary that will hold old and new names


with open("names_rev.txt") as f: #fill dictionary
    for line in f:
       (old, new) = line.split()
       dic[(old)] = new
       
oldpdb = open("Erg1.pdb", 'r') 
newpdb = open("replaced_Erg1.pdb", 'w')

for line in oldpdb:
	original = line
	for i, j in dic.items():
		if i in line:
			if original == line and line[line.rindex(i) +1].isspace():	# make sure old hasn't already been replaced, and make sure entire key is replaced
				line = line.replace(i,j)		#replace old with new
	newpdb.write(line)
	
