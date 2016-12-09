import subprocess
lookup_user = 'root'
processes_running = 0

def activeProcesses(lookup_user, lookup_cmd):
	processes_running_all = 0
	processes_running_searched = 0
	for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
		user = line.split()[0]
		if lookup_user == user:
			processes_running_all +=1
			if lookup_cmd in line:
				processes_running_searched += 1
	return processes_running_all, processes_running_searched

procs_total, procs_searched = activeProcesses('root', 'aws')

print procs_total, procs_searched


