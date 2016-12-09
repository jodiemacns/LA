import subprocess

users = {}

ps_cmd = subprocess.check_output(['ps', '-ef'])
ps_cmd_split = ps_cmd.splitlines()

#print ps_cmd

for line in ps_cmd_split [1:]:
	user = line.split()[0]
	if users.get(user):
		users[user] += 1
	else:
		users[user] = 1

print "Active users on the system are " + ','.join(users.keys())

for user, process_count in users.items():
	print "%s is running %s processes" %(user, process_count)

print "------------- And -----------------"
users = {}

for line in ps_cmd.splitlines() [1:]:
	user = line.split()[0]
	users[user] = users.get(user,0) + 1

print "Active users on the system are " + ','.join(users.keys())
for user, process_count in users.items():
	print "%s is running %s processes" %(user, process_count)
