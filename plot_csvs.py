import csv
import matplotlib.pyplot as plt


total_reqs = {}	# col 2
total_failures = {}	#col 3
average_RT = {}	# col 5
max_RT = {}	# col 7
rps = {}	# col 8
max_total_reqs = 0
max_total_failures = 0
max_avg_rt = 0
max_max_rt = 0
max_rps = 0

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
	platforms = ["gcp", "aws", "azure"]
	for idx, platform in enumerate(platforms):
		num_clients = [50, 100, 300, 500, 700, 800, 900, 1000, 1030, 1060, 1090, 1120, 1150, 1180, 1210, 1240, 1270, 1300, 1330, 1360, 1390, 1420, 1450, 1480, 1510, 1600]
		for n in num_clients:
			csv_name = "logs_"+platform+"/log_"+str(n)+"_requests.csv"
			csv_file = open(csv_name)
			extract_params(csv_file, platform)


	print("total_reqs: ", total_reqs)
	print("total_failures: ", total_failures)
	print("average_RT: ", average_RT)
	print("max_RT: ", max_RT)
	print("rps: ", rps)

	plt.plot(num_clients, rps["gcp"], color= 'r', label="GCP")
	plt.plot(num_clients, rps["aws"], color='g', label="AWS")
	plt.plot(num_clients, rps["azure"], color='b', label="Azure")
	plt.xlabel("Clients")
	plt.ylabel("RPS")
	plt.xlim(0, 2000)
	plt.ylim(0, max(max(rps["gcp"]), max(rps["aws"]), max(rps["azure"]))+50)
	plt.legend(loc='upper right')
	plt.savefig("Clients_RPS.png")

	plt.clf()
	plt.plot(num_clients, total_failures["gcp"], color='r', label="GCP")
	plt.plot(num_clients, total_failures["aws"], color='g', label="AWS")
	plt.plot(num_clients, total_failures["azure"], color='b', label="Azure")
	plt.xlabel("Clients")
	plt.ylabel("Failures")
	plt.xlim(0, 2000)
	plt.ylim(0, max(max(total_failures["gcp"]), max(total_failures["aws"]), max(total_failures["azure"]))+100)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Failure.png")

	plt.clf()
	plt.plot(num_clients, average_RT["gcp"], color='r', label="GCP")
	plt.plot(num_clients, average_RT["aws"], color='g', label="AWS")
	plt.plot(num_clients, average_RT["azure"], color='b', label="Azure")
	plt.xlabel("Clients")
	plt.ylabel("Average Resp Time")
	plt.xlim(0, 2000)
	plt.ylim(0, max(max(average_RT["gcp"]), max(average_RT["aws"]), max(average_RT["azure"]))+200)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Avg_RT.png")


	plt.clf()
	plt.plot(num_clients, max_RT["gcp"], color='r', label="GCP")
	plt.plot(num_clients, max_RT["aws"], color='g', label="AWS")
	plt.plot(num_clients, max_RT["azure"], color='b', label="Azure")
	plt.xlabel("Clients")
	plt.ylabel("Maximum Resp Time")
	plt.xlim(0, 2000)
	plt.ylim(0, max(max(max_RT["gcp"]), max(max_RT["aws"]), max(max_RT["azure"]))+200)
	plt.legend(loc='upper right')
	plt.savefig("Clients_Max_RT.png")

