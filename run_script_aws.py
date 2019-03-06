import os
#import subprocess

def execute_commands():
	num_clients = [50, 100, 300, 500, 700, 800, 900, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1460, 1480, 1500, 1600, 1700]


	for n in num_clients:
		hatch_rate = n/10
		time = 10+60

		command = "locust --host=http://54.198.63.141/ -t "+ str(time)+"s --no-web -c "\
		+str(n)+" -r "+str(hatch_rate)+" --csv=logs_aws/log_"+str(n)+" --port 811"
		os.system(command)


if __name__ == "__main__":
	execute_commands()
