import subprocess

# Create a dictionary called user.
# --------------------------------
# Each key is separated from its value by a colon (:), the items are separated 
# by commas, and the whole thing is enclosed in curly braces. An empty 
# dictionary without any items is written with just two curly braces, like 
# this: {}.
# Keys are unique within a dictionary while values may not be. The values of a 
# dictionary can be of any type, but the keys must be of an immutable data type 
# such as strings, numbers, or tuples.
users = {}

# Set Get the output of the command "ps -ef"
# UID        PID  PPID  C STIME TTY          TIME CMD
# root     27704     2  0 21:10 ?        00:00:00 [kworker/u2:0]
# jodie    27762 27555  0 21:15 pts/0    00:00:01 vim activeuser.py
ps_cmd = subprocess.check_output(['ps', '-ef'])

# Split the multiple lines into a list of strings.
# The method splitlines() returns a list with all the lines in string, 
# optionally including the line breaks (if num is supplied and is true)
ps_cmd_split = ps_cmd.splitlines()

print ps_cmd_split[1].split()[0]
print ps_cmd_split[2].split()[0]
#print ps_cmd_split[1]
#exit()

# Assign line to each of the list items.
# The first line is the header
for line in ps_cmd_split [1:]:
    # Get the user which is in the first item of the list of the line.
	user = line.split()[0]
    # If the key "The user name" is found increment the number of users.
	if users.get(user):
		users[user] += 1
    # If the user is not there assign the new key to be set to 1.
	else:
		users[user] = 1

# Print the unique users in the system.
print "Active users on the system are " + ','.join(users.keys())

#dict.items() returns a list of 2-tuples ( [(key, value), (key, value), ...] )
for user, process_count in users.items():
	print "%s is running %s processes" %(user, process_count)

print "------------- And -----------------"
users = {}

# Just another way to fill in all the users like above.
for line in ps_cmd.splitlines() [1:]:
	user = line.split()[0]
    # the second paramater is the default return if it does not exist.
    # So here it will be the num + 1 if exist, and 0 + 1 if it does not.
	users[user] = users.get(user,0) + 1

print "Active users on the system are " + ','.join(users.keys())
for user, process_count in users.items():
	print "%s is running %s processes" %(user, process_count)
