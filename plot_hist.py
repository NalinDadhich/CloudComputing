import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
	platforms = ["gcp", "aws", "azure"]
	for idx, platform in enumerate(platforms):
		percentiles = [50, 66, 75, 80, 90, 95, 98, 99, 100, 0]
		if platform == "gcp":
			csv_name = "logs_"+platform+"_random/log_1090_distribution.csv"
		elif platform == "aws":
			csv_name = "logs_"+platform+"_random/log_1150_distribution.csv"
		else:
			csv_name = "logs_"+platform+"_random/log_1120_distribution.csv"

		csv_file = open(csv_name)
		csv_reader = csv.reader(csv_file, delimiter=',')
		time = []
		time.append(0)
		for row in csv_reader:
			if "GET" in row[0]:
				for col in range(2,11):
					time.append(float(row[col]))
		print(time)
		plt.clf()
		# plt.hist(time,weights=percentiles) # A bar chart
		plt.xlabel('Time (in ms)')
		plt.ylabel('Percentage of requests completed')
		plt.ylim(0, 100)
		plt.xlim(0, time[-1])
		if platform is "gcp":
			plt.title('Average behavior of GCP when failure first occurs')
		elif platform is "aws":
			plt.title('Average behavior of AWS when failure first occurs')
		else:
			plt.title('Average behavior of Azure when failure first occurs')
		
		data = time
		for i in range(len(data)):
			data[i] += 0.5
		plt.hist(data, bins=time, weights=percentiles, edgecolor='red')
		name = "Hist_"+platform+".png"
		plt.savefig(name)