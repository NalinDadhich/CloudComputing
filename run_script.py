import os
import subprocess

def execute_commands():
	num_clients = [1, 5, 200, 1000, 2000]
	hatch_rate = 1
	for n in num_clients:
		command = "locust --host=http://cloudcomputingapp.azurewebsites.net/ --port 8090 -t 300s --no-web -c "\
		+str(n)+" -r "+str(hatch_rate)+" --csv=log_"+str(n)+"_"+str(hatch_rate)
		os.system(command)

if __name__ == "__main__":
	execute_commands()