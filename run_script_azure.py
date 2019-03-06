import os
#import subprocess

def execute_commands():
	num_clients = [1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1460, 1480, 1500]


	for n in num_clients:
		hatch_rate = n/10
		time = 10+60

		command = "locust --host=http://52.179.0.251/ -t "+ str(time)+"s --no-web -c "\
		+str(n)+" -r "+str(hatch_rate)+" --csv=logs_azure/log_"+str(n)+" --port 809"
		os.system(command)


if __name__ == "__main__":
	execute_commands()
