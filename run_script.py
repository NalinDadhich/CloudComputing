import os
import subprocess

def execute_commands():
	num_clients = [400, 450, 500, 700, 1000]
	
	
	for n in num_clients:
		hatch_rate = n/10
		time = 10+30

		command = "locust --host=http://40.122.64.116/ -t "+ str(time)+"s --no-web -c "\
		+str(n)+" -r "+str(hatch_rate)+" --csv=logs/log_"+str(n)+" --port 809"
		os.system(command)

if __name__ == "__main__":
	execute_commands()