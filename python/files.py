filename = '/var/log/secure'

# Line by line is the prefered way.
for line in open(filename):
	print line

# Whole file aka slurping
with open(filename) as file_handle:
	lines = file_handle.readlines()
	for line in lines:
		print("-->" + line)

filename = 'testfile.txt'
with open(filename, 'w') as file_handler:
	file_handler.write("here is text\n")

with open(filename, 'a') as file_handler:
	file_handler.write("here is more text\n")

import csv
file_handle = open('j.csv')
reader = csv.reader(file_handle)
os_counts = {}

for row in reader:
	os_counts[row[2]] = os_counts.get(row[2], 0)+1

print "counts = " + str(os_counts)


try:
	filename = '/var/log/notthere'
	for line in open(filename):
		print line
except IOError:
	print "File does not exist"
except:
	print "Can't open file for other reason"
else:
	print "Done processing file"
