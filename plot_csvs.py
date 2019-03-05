import csv
import matplotlib.pyplot as plt


total_reqs = []	# col 2
total_failures = []	#col 3
average_RT = []	# col 5
max_RT = []	# col 7
rps = []	# col 8

def extract_params(csv_file):
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		if "GET" in row[0]:
			print(row)
			total_reqs.append(float(row[2]))
			total_failures.append(float(row[3]))
			average_RT.append(float(row[5]))
			max_RT.append(float(row[7]))
			rps.append(float(row[-1]))

if __name__ == "__main__":
	num_clients = [10, 30, 50, 100, 150, 200, 250, 300, 350, 400, 450]
	for n in num_clients:
		csv_name = "logs/log_"+str(n)+"_requests.csv"
		csv_file = open(csv_name)
		extract_params(csv_file)

	print("total_reqs: ", total_reqs)
	print("total_failures: ", total_failures)
	print("average_RT: ", average_RT)
	print("max_RT: ", max_RT)
	print("rps: ", rps)

	plt.plot(rps, average_RT)
	plt.xlabel("RPS")
	plt.ylabel("average RT")
	plt.savefig("ABC.png")


