import random

results = {'heads' : 0, 'tails' : 0}

for i in range (0,1000):
	toss = random.randint(0,2)
	if toss == 1:
		results['heads'] += 1
	else:
		results['tails'] += 1

for toss in results.keys():
	print "coinface %s showed up %s times" %(toss, results[toss])

print results

