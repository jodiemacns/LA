list1 = [1,2,3,4]
print list1

list2 = range(1,19)
print list2

list2 = ['a', 'b', 'c', 'd']
print list2

list3 = [1,62,"q", "I am also a member"]
print list3

str1 = "joe"
list4 = ["4", 'Apple', str1]

print "list4[2] = " + str(list4[2])

print "Partial = " + str(list4[1:])

list4.append('George')
print 'added George:' + str(list4)

people = ["jet", "donny", "jerome", "paul"]
print people[2]

print people
print 'index of donny = ' + str(people.index('donny'))
people.remove('donny')
print 'Remove donny'
print people

print 'Insert ben before paul'
people.insert(people.index('paul'), 'ben')
print people

#-----------------------------------------------
import subprocess

partition_usage_threshold = 5

df_cmd = subprocess.check_output(['df','-k'])
print df_cmd

lines = df_cmd.splitlines()

print lines
for line in lines[1:]:
	columns = line.split()
	used_percentage = columns[4]
	used_percentage = used_percentage.replace('%','')
	if int(used_percentage) >= partition_usage_threshold:
		print "partition %s usage is beyond threshold at %s " % (columns[0], columns[4])

