import urllib
import json

url = "https://labfiles.linuxacademy.com/python/ec2-response.json"
response = urllib.urlopen(url)
json_string = response.read()

print json_string

data = None
data = json.loads(str(json_string))

try:
	data = json.loads(str(json_string))
except:
	data = None
	print 'No Data!!'

if( data ):
	print "InstanceID %s is %s " %(data['InstanceStatuses'][0]['InstanceId'], data['InstanceStatuses'][0]['InstanceState']['Name'])
	print "InstanceID %s Details are %s " %(data['InstanceStatuses'][0]['InstanceId'], data['InstanceStatuses'][0]['InstanceStatus']['Details'])

#InstanceID i-1234567890abcdef0 is running
#{
#    "InstanceStatuses": [
#        {
#            "InstanceId": "i-1234567890abcdef0",
#            "InstanceState": {
#                "Code": 16,
#                "Name": "running"
#            },
#            "AvailabilityZone": "us-east-1d",
#            "SystemStatus": {
#                "Status": "ok",
#                "Details": [
#                    {
#                        "Status": "passed",
#                        "Name": "reachability"
#                    }
#                ]
#            },
#            "InstanceStatus": {
#                "Status": "ok",
#                "Details": [
#                    {
#                        "Status": "passed",
#                        "Name": "reachability"
#                    }
#                ]
#            }
#        }
#    ]

#----------------------------
# Now create a json structure.
data = {
	'course_name' : 'python',
	'videos' :['strings', 'classes', 'json'],
	'id' : 5
}

json_string = json.dumps(data, indent=4)

print json_string

print 'Now to remove the spaces for faster transmission'

json_string = json.dumps(data)
print json_string

