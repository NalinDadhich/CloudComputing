import csv
import matplotlib.pyplot as plt

total_failures = []
total_reqs = []
median_response_time = []
requests_per_sec = []

def extract_params(csv_file):
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		if "GET" in row[0]:
			print(row)
			total_reqs.append(float(row[2]))
			total_failures.append(float(row[3]))
			median_response_time.append(float(row[4]))
			requests_per_sec.append(float(row[-1]))
			print("~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
	num_clients = [1, 5, 200]
	
	for n in num_clients:
		csv_name = "temp"+str(n)+"_requests.csv"
		csv_file = open(csv_name)
		extract_params(csv_file)
		print("total_reqs: ", total_reqs)
		print("total_failures: ", total_failures)
		print("median_response_time: ", median_response_time)
		print("requests_per_sec: ", requests_per_sec)

	plt.xlabel("Total Requests")
	plt.ylabel("Total Failures")
	plt.plot(total_reqs, total_failures)
	plt.savefig('total_failures.png')
	plt.clf()

	plt.plot(total_reqs, median_response_time)
	plt.xlabel("Total Requests")
	plt.ylabel("Median Response Time")
	plt.xlim(0, 300)
	plt.ylim(30, 40)
	plt.savefig('median_response_time.png')
	plt.clf()

	plt.plot(total_reqs, requests_per_sec)
	plt.xlabel("Total Requests")
	plt.ylabel("Requests per sec")
	plt.ylim(0, 100)
	plt.savefig('requests_per_sec.png')
	plt.clf()


