""" This example uses Pyton Fabric to deploy MySQL/MaraDB and Apache on five servers """
# yum install fabric
# To run: fab deploy
#
# import all the fabric functions that we need explicity
from fabric.api import env, roles, sudo, execute, put, run, local, lcd, prompt, cd, parallel

# import the os module to ge file basenames
import os

# define groups of webservers and databases
env.roledefs = {
	"webserver" : [ "54.89.225.29", "54.89.11.33", "54.144.126.0" ], 
	"database"  : [ "54.152.109.249", "54.158.85.233"] 
}

#define a special group called all so we can easily send out commands to all servers if needed.
env.roledefs["all"] = [h for r in env.roledefs.values() for h in r ]

# The packages that are required to run our application on the server groups
packages_required = {
	"webserver" : [ "httpd", "php", "ntp", "php-mysqli"],
	"database"  : [ "mariadb-server" ]
}

# Filese that need to be downloaded form the labserver repo
download_files = {
	"database" : ["http://labfiles.linuxacademy.com/python/fabric/sakila.sql",
			"http://labfiles.linuxacademy.com/python/fabric/sakila-data.sql"],
	"webserver" : ["http://labfiles.linuxacademy.com/python/fabric/sakila.sql"]
} 

@roles("database") # this decorater will make the function following it run for all dabase group server
def install_database():
	# install the database application
	# sudo is used when you need to run a cmd on the remote server as superuser.
	sudo("yum -y install %s" % " ".join(packages_required["database"]),pty=True)

	#active MySQL/MariDB in the system control.
	sudo("systemctl enable mariadb", pty=True)

	# Start MySQL/MariDB using the system control
	sudo("systemctl start mariadb", pty=True)

	# Create a user on the database the we will be using from our webservers
	sudo(r""" mysql -h 127.0.0.1 -u root -e "CREATE USER 'web'@'%' IDENTIFIED BY 'web'; GRANT ALL PRIVILEGES ON *.* TO 'web'@'%'; FLUSH PRIVILEGES; " """)

	# Check for the mysql process is running
	# This is how you run a command when you do not need super user
	run("ps -ef | grep mysql")

@parallel
@roles("database") # This decorater will make the function following it run for all database group server.
def setup_database():
	#setup the tmp directory where we will download files from the web
	tmpdir = "/tmp"

	# This cd is the fabric command to change directory on the remote server
	with cd(tmpdir): # cd changes the dir on the remote server

		# Iterate over the files we need to download for the database
		for url in download_files["database"]:
			# Vasename gives us just the name of the file, without any path info, it also works for urls
			filename = "%s/%s" %(tmpdir, os.path.basename(url));i
		
			#useing the function tun on the rmote server, we can execute commands, in the case 
			#wge which opens the url and save it to filename
			run("wget --no-cache %s -O %s" % (url, filename))
		
			# Since these are SQL files, we can just dump them into out MySQL/MariaDB server
			run("mysql -u root < %s" % filename)

@roles("webserver") # This decorater will make the function folling it run for all the webserver group
def install_webserver():
	# Install the webserver applications
	# sudo is used when you need to run a cmd on the remote server as su
	su("yum -y install %s" % " ".join(packages_required["wevserver"]),pty=True)

	# active and start httpd
	sudo("systemctl enable httpd.service", pty=True)
	sudo("systemctl start gttpd.service", pty=True)

	# Here are some SElinux commands to get this working.
	sudo("setsebool -P httpd_can_network_connect=1", pty=True)
	sudo("setsebool -P httpd_read_user_content=1", pty=True)

@roles("webserver") # This decorater will make the function folling it run afor all wevserver group ser
def setup_webserver():
	#setup the tmp directory
 	tmpdir = "/tmp"

	# Directory on the remote server
	remote_dir = "/var/www/html"

	# This time we will download the files on our master server and then put them on the
	# remote server to see the functionality.
	with lcd(tmpdir):
		# Iterate over the files we need to download for the webserver
		for url in download_files["webserver"]:
			# Basename gives us just the name of the file, without any path information,
			# it also works for urls	
			filename = "%s/%s" %(tmpdir, os.path.basename(url))
	
			# Local runs the command locally on our local server
			local("wget --no-cache %s =O %s" % (url, filename))
	
			# And put sends a file from the local server to remote server
			# we can also change the running permissions
			# and use sudo if required
			put(filename, "/var/www/html/", mode=0775, use_sudo=True)
	
	# The webserver need to connect to a database in the back
	database = pick_sever(env.roledefs["database"])\
	
	# Again using sudo, we can just create a file on the remote server,
	# and put in the database server we got back from the function
	sudo(r""" echo " <?php \\%db = '%s'; ?> " > /var/www/html/db.php """ % env.roledefs['database'][database])

def pick_server(mylist):
	# Simple function that takes a list and enumerates it
	# And asks the user to select a valid member from the list
	database = 0
	while not 1<=database<=len(mylist):
		for i, db in enumerate(mylist, 1):
			print '*'*10
			for i, db in enumerate(mylist,1):
				print "[%s] - %s" % (i, db)
			database = prompt("Enter the number of the database should I connect %s to:   " % (env.host), validate=int)
			return int(database)-1

@roles("all")
def upgrade_servers():
	#Just doing a upgrade on the CentOS
	sudo("yum -y upgrade", pty=True)

# This is the main function we will be calling to get it all running
def deploy():
	#Note here that the execute function has the names of the functions we 
	# are not calling, but we are excluding the parenthesis()
	execute(upgrade_servers)
	execute(install_database)
	execute(install_webserver)
	execute(setup_database)
	execute(setup_webserver)
	print "Rock and Roll!!"

		
