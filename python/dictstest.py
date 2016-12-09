# >>> execfile('dictstest.py')
# {'green': 'go', 'yellow': 'about to go', 'red': 'stop'}
# Coinface tails showed up 634 times
# Coinface heads showed up 366 times
# Active users on the system are colord,polkitd,postfix,dbus,chrony,rpc,user,avahi,rtkit,root
# colord is running 1 processes
# polkitd is running 1 processes
# postfix is running 2 processes
# dbus is running 1 processes
# chrony is running 1 processes
# rpc is running 1 processes
# user is running 42 processes
# avahi is running 2 processes
# rtkit is running 1 processes
# root is running 105 processes
# john is not in there
# {'colord': 2, 'polkitd': 2, 'postfix': 4, 'dbus': 2, 'chrony': 2, 'rpc': 2, 'user': 84, 'avahi': 4, 'rtkit': 2, 'root': 105}

import random
import subprocess

traffic_signal = {}
traffic_signal['red']    = 'stop'
traffic_signal['yellow'] = 'about to go'
traffic_signal['green']  = 'go'

traffic_signal = { 'red' :  'stop', 'yellow' : 'about to go', 'green' : 'go'}
print traffic_signal

results = {'heads' : 0, 'tails' : 0}
for i in range(0, 1000):
	toss = random.randint(0,2)
	if toss == 1:
		results['heads'] +=1
	else:
		results['tails'] += 1

for toss in results.keys():
	print "Coinface %s showed up %s times" %(toss, results[toss])

users = {}
ps_cmd = subprocess.check_output(['ps', '-ef'])

for line in ps_cmd.splitlines()[1:]:
	user = line.split()[0]
	if users.get(user):
		users[user]+=1
	else:
		users[user]=1

print "Active users on the system are " + ','.join(users.keys())

for user, process_count in users.items():
	print "%s is running %s processes" % (user, process_count)

del users['root']

print users.get('john', 'john is not in there')

for line in ps_cmd.splitlines()[1:]:
	user = line.split()[0]
	users[user]=users.get(user,0)+1

print users
