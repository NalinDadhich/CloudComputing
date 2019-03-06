import os
#import subprocess

def execute_commands():
	num_clients = [50, 100, 300, 500, 700, 800, 900, 1000, 1030, 1060, 1090, 1120, 1150, 1180, 1210, 1240, 1270, 1300, 1330, 1360, 1390, 1420, 1450, 1480, 1510, 1600]

	for n in num_clients:
		hatch_rate = n/10
		time = 10+60

		command = "locust --host=http://52.179.0.251/ -t "+ str(time)+"s --no-web -c "\
		+str(n)+" -r "+str(hatch_rate)+" --csv=logs_azure/log_"+str(n)+" --port 809"
		os.system(command)


if __name__ == "__main__":
	execute_commands()
