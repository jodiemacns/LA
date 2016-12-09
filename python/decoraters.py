import time
import urllib2

def download_webpage():
	url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
	response = urllib2.urlopen(url, timeout = 60)
	return response.read()

def elapsed_time():
	t0 = time.time()
	webpage = download_webpage()
	t1 = time.time()
	print "Elapsed time: %s\n" % (t1- t0)

elapsed_time()

def d_elapsed_time(function_to_time):
	def wrapper():
		t0 = time.time()
		function_to_time()
		t1 = time.time()
		print "Elapsed time (d): %s\n" % (t1 - t0)
	return wrapper

@d_elapsed_time
def d_download_webpage():
	url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
	response = urllib2.urlopen(url, timeout = 60)
	return response.read()

webpage = d_download_webpage()

@d_elapsed_time
def another_function():
	print "Doing something else"
	for i in range(1,1000000):
		pass

another_function()

