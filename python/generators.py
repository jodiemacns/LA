def counter():
	i=0
	while True:
		i+=1
		return i

a = counter()
print a

print "-------- Now the generators -------" 
def counter_generator():
	i=0
	while True:
		i+=1
		yield i

a = counter_generator()
print "-------- Now the printing -------" 
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
