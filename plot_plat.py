import csv
import matplotlib.pyplot as plt


total_reqs = {}	# col 2
total_failures = {}	#col 3
average_RT = {}	# col 5
max_RT = {}	# col 7
rps = {}	# col 8

def extract_params(csv_file, platform):
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		if "GET" in row[0]:
			print(row)
			if platform not in total_reqs.keys():
				total_reqs[platform] = []
				total_failures[platform] = []
				average_RT[platform] = []
				max_RT[platform] = []
				rps[platform] = []


			total_reqs[platform].append(float(row[2]))
			total_failures[platform].append(float(row[3]))
			average_RT[platform].append(float(row[5]))
			max_RT[platform].append(float(row[7]))
			rps[platform].append(float(row[-1]))

if __name__ == "__main__":
	num_clients = [50, 100, 300, 500, 700, 800, 900, 1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1460, 1480, 1500, 1600, 1700]
	#num_clients = [1000, 1020, 1040, 1060, 1080, 1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360]
	# num_clients = [50, 100, 300, 500, 700, 800, 900, 1000, 1030, 1060, 1090, 1120, 1150, 1180, 1210, 1240, 1270, 1300, 1330, 1360, 1390, 1420, 1450, 1480, 1510, 1600]
	platform = "gcp"
	for n in num_clients:
		csv_name = "logs_gcp1/log_"+str(n)+"_requests.csv"
		csv_file = open(csv_name)
		extract_params(csv_file, platform)


	print("total_reqs: ", total_reqs)
	print("total_failures: ", total_failures)
	print("average_RT: ", average_RT)
	print("max_RT: ", max_RT)
	print("rps: ", rps)

	plt.plot(num_clients, rps[platform], color= 'r', label="GCP")
	plt.xlabel("Clients")
	plt.ylabel("RPS")
	plt.xlim(0, 2000)
	plt.ylim(0, max(rps[platform])+50)
	plt.legend(loc='upper right')
	plt.savefig("Clients_RPS.png")

	plt.clf()
	plt.plot(num_clients, total_failures[platform], color='r', label="GCP")
	plt.xlabel("Clients")
	plt.ylabel("Failures")
	plt.xlim(0, 2000)
	plt.ylim(0, max(total_failures[platform])+100)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Failure.png")

	plt.clf()
	plt.plot(num_clients, average_RT[platform], color='r', label="GCP")
	plt.xlabel("Clients")
	plt.ylabel("Average Resp Time")
	plt.xlim(0, 2000)
	plt.ylim(0, max(average_RT[platform])+200)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Avg_RT.png")


	plt.clf()
	plt.plot(num_clients, max_RT[platform], color='r', label="GCP")
	plt.xlabel("Clients")
	plt.ylabel("Maximum Resp Time")
	plt.xlim(0, 2000)
	plt.ylim(0, max(max_RT[platform])+200)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Max_RT.png")

