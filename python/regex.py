# Regular expression
# /var/log/secure on centos
# faild password / auth failure email to stop.
# Note: tmux copy paste 1. ctrl b [ 2. ctrl space 3. alt w 4. ctrl b ctrl ]
# Good link: http://www.pyregex.com/
import re

# Sample line from the log file.
# Dec  7 17:45:30 jodiemacns1 sshd[5458]: Failed password for user from 142.167.35.138 port 56136 ssh2
line = "Dec  7 17:45:30 jodiemacns1 sshd[5458]: Failed password for user from 142.167.35.138 port 56136 ssh2"

# test the line find sshd
match = re.search('sshd', line)
print 'match = ' + str(match)

# test the line mismatch. (there is no hello_
match = re.search('hello', line)
print 'match = ' + str(match)

line = "Dec  7 17:45:30 jodiemacns1 sshd[5458]: Failed password for user from 142.167.35.138 port 56136 ssh2"
#                             
#                             +-2 characters lower case 
#                             | +- 1 - 2 Space
#                             | |      +- dd:dd:dd (date: 2 digits: ...)
#                             | |      |                          +- Space
#                             | |      |                          | +- letters of numbers, * meaning til not
#                             | |      |                          | | + Space followed by 'sshd'
#                             | |      |                          | | |      +-- [num any length]: .. [5458] in example
#                             | |      |                          | | |      |                           +- One or more letters or numbers
#                             | |      |                          | | |      |                           |       +-- ip address 1-3 digits set of 4
#                             | |      |                          | | |      |                           |       |
#                             | |_____ |_______________           | | |____  |_____                      |       |_________________________________
#                    D   ec   | |     ||               |          | | |    | |     |                     |       |                                 |
match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w*\ssshd\[\d*\]: Failed password for \w+ from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2', line)
print 'match = ' + str(match)
# appending ? at the end of the match makes it non greedy. 
# allowing it to continue until the next group match is found.
#                     |      |                                 |
match = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$',line)
print match.groups()
print match.group(1)
print match.group(2)
print match.group(3)
